from functools import partial
from typing import Any, Dict, List

from tartiflette.parser.cffi import (
    Visitor,
    _VisitorElement,
    _VisitorElementOperationDefinition,
    _VisitorElementSelectionSet,
)
from tartiflette.parser.nodes.field import NodeField
from tartiflette.parser.nodes.fragment_definition import NodeFragmentDefinition
from tartiflette.parser.nodes.operation_definition import (
    NodeOperationDefinition,
)
from tartiflette.parser.nodes.variable_definition import NodeVariableDefinition
from tartiflette.parser.visitor.visitor_context import InternalVisitorContext
from tartiflette.schema import GraphQLSchema
from tartiflette.types.exceptions.tartiflette import (
    AlreadyDefined,
    InvalidType,
    MultipleRootNodeOnSubscriptionOperation,
    NotLoneAnonymousOperation,
    NotUniqueOperationName,
    UndefinedFragment,
    UnknownSchemaFieldResolver,
    UnknownTypeDefinition,
    UnknownVariableException,
    UnusedFragment,
)
from tartiflette.types.helpers import reduce_type


class InlineFragmentInfo:
    def __init__(self, atype, depth):
        self.type = atype
        self.depth = depth


class TartifletteVisitor(Visitor):
    # pylint: disable=too-many-instance-attributes

    def __init__(
        self, schema: GraphQLSchema, variables: Dict[str, Any] = None
    ):
        super().__init__()
        self._events = [
            {
                "default": self._in,
                "Argument": self._on_argument_in,
                "Field": self._on_field_in,
                "Variable": self._on_variable_in,
                "IntValue": self._on_value_in,
                "StringValue": self._on_value_in,
                "BooleanValue": self._on_value_in,
                "FloatValue": self._on_value_in,
                "NamedType": self._on_named_type_in,
                "ListType": self._on_list_type_in,
                "NonNullType": self._on_non_null_type_in,
                "VariableDefinition": self._on_variable_definition_in,
                "FragmentDefinition": self._on_fragment_definition_in,
                "OperationDefinition": self._on_operation_definition_in,
                "InlineFragment": self._on_inline_fragment_in,
                "SelectionSet": self._on_selection_set_in,
            },
            {
                "default": self._out,
                "Document": self._on_document_out,
                "Argument": self._on_argument_out,
                "Field": self._on_field_out,
                "VariableDefinition": self._on_variable_definition_out,
                "FragmentDefinition": self._on_fragment_definition_out,
                "FragmentSpread": self._on_fragment_spread_out,
                "OperationDefinition": self._on_operation_definition_out,
                "InlineFragment": self._on_inline_fragment_out,
            },
        ]

        self._named_operations = {}
        self._anonymous_operations = []
        self.root_nodes = []
        self._vars = variables if variables else {}
        self._fragments = {}
        self._used_fragments = set()
        self.schema: GraphQLSchema = schema
        self.exceptions: List[Exception] = []
        self._to_call_later = []
        self._internal_ctx = InternalVisitorContext()

    def _add_exception(self, exception, continue_child=0):
        self.continue_child = continue_child
        self.exceptions.append(exception)

    def _on_argument_in(self, element: _VisitorElement, *_args, **_kwargs):
        self._internal_ctx.argument_name = element.name

    def _on_argument_out(self, *_args, **_kwargs):
        self._internal_ctx.argument_name = None

    def _on_value_in(self, element: _VisitorElement, *_args, **_kwargs):
        if hasattr(self._internal_ctx.node, "default_value"):
            self._internal_ctx.node.default_value = element.get_value()
            return

        self._internal_ctx.node.arguments.update(
            {self._internal_ctx.argument_name: element.get_value()}
        )

    def _on_variable_in(self, element: _VisitorElement, *_args, **_kwargs):
        if hasattr(self._internal_ctx.node, "var_name"):
            self._internal_ctx.node.var_name = element.name
            return

        try:
            var_name = element.name
            self._internal_ctx.node.arguments.update(
                {self._internal_ctx.argument_name: self._vars[var_name]}
            )
        except KeyError:
            self._add_exception(UnknownVariableException(var_name))

    def _on_field_in(
        self, element: _VisitorElement, *_args, type_cond_depth=-1, **_kwargs
    ):  # pylint: disable=too-many-locals
        type_cond = self._internal_ctx.compute_type_cond(type_cond_depth)
        field = None

        try:
            parent_type = reduce_type(
                self._internal_ctx.node.field_executor.schema_field.gql_type
            )
        except (AttributeError, TypeError):
            parent_type = self.schema.find_type(
                self.schema.get_operation_type(
                    self._internal_ctx.operation.type
                )
            )

        try:
            field = self.schema.get_field_by_name(
                str(parent_type) + "." + element.name
            )
        except UnknownSchemaFieldResolver as e:
            try:
                if type_cond is None:
                    raise
                field = self.schema.get_field_by_name(
                    str(type_cond) + "." + element.name
                )
            except UnknownSchemaFieldResolver as e:
                if (
                    self._internal_ctx.node is None
                    or self._internal_ctx.node.field_executor is not None
                ):
                    e.path = self._internal_ctx.field_path[:] + [element.name]
                    e.locations = [element.get_location()]
                    self._add_exception(e, 1)

        self._internal_ctx.move_in_field(element)

        node = NodeField(
            element.name,
            self.schema,
            field.resolver if field else None,
            element.get_location(),
            self._internal_ctx.field_path[:],
            type_cond,
            element.get_alias(),
        )

        node.set_parent(self._internal_ctx.node)
        if self._internal_ctx.node:
            self._internal_ctx.node.add_child(node)

        self._internal_ctx.node = node

        if self._internal_ctx.depth == 1:
            self.root_nodes.append(node)

    def _on_field_out(self, *_args, **_kwargs):
        self._internal_ctx.move_out_field()

    def _on_variable_definition_in(
        self, element: _VisitorElement, *_args, **_kwargs
    ):
        node = NodeVariableDefinition(
            self._internal_ctx.path, element.get_location(), element.name
        )
        node.set_parent(self._internal_ctx.node)
        self._internal_ctx.node = node

    def _validate_type(self, varname, a_value, a_type):
        try:
            if not isinstance(a_value, a_type):
                self._add_exception(
                    InvalidType(
                        "Given value for < %s > is not type < %s >"
                        % (varname, a_type),
                        path=self._internal_ctx.field_path[:],
                        locations=[self._internal_ctx.node.location],
                    )
                )
        except TypeError:
            # TODO remove this, and handle the case it's an InputValue
            # (look at registered input values and compare fields)
            pass

    def _validates_vars(self):
        # validate given var are okay
        name = self._internal_ctx.node.var_name
        if name not in self._vars:
            dfv = self._internal_ctx.node.default_value
            if not dfv and not self._internal_ctx.node.is_nullable:
                self._add_exception(UnknownVariableException(name))
                return None

            self._vars[name] = dfv
            return None

        a_type = self._internal_ctx.node.var_type
        a_value = self._vars[name]

        if self._internal_ctx.node.is_list:
            if not isinstance(a_value, list):
                self._add_exception(
                    InvalidType(
                        "Expecting List for < %s > values" % name,
                        path=self._internal_ctx.field_path[:],
                        locations=[self._internal_ctx.node.location],
                    )
                )
                return None

            for val in a_value:
                self._validate_type(name, val, a_type)
            return None

        self._validate_type(name, a_value, a_type)
        return None

    def _on_variable_definition_out(self, *_args, **_kwargs):
        self._validates_vars()
        # now the VariableDefinition Node is useless so kill it
        self._internal_ctx.node = self._internal_ctx.node.parent

    def _on_named_type_in(self, element: _VisitorElement, *_args, **_kwargs):
        try:
            self._internal_ctx.node.var_type = element.name
        except AttributeError:
            pass

    def _on_list_type_in(self, *_args, **_kwargs):
        try:
            self._internal_ctx.node.is_list = True
        except AttributeError:
            pass

    def _on_non_null_type_in(self, *_args, **_kwargs):
        self._internal_ctx.node.is_nullable = False

    def _on_fragment_definition_in(
        self, element: _VisitorElement, *_args, **_kwargs
    ):
        if element.name in self._fragments:
            self._add_exception(
                AlreadyDefined(
                    "Fragment < %s > already defined" % element.name,
                    path=self._internal_ctx.field_path[:],
                    locations=[element.get_location()],
                )
            )
            return

        type_condition = element.get_type_condition()
        if not self.schema.has_type(type_condition):
            self._add_exception(
                UnknownTypeDefinition(
                    "Unknown type < %s >." % type_condition,
                    locations=[element.get_location()],
                )
            )
            return

        nfd = NodeFragmentDefinition(
            self._internal_ctx.path,
            element.get_location(),
            element.name,
            type_condition=type_condition,
        )

        self._internal_ctx.fragment_definition = nfd
        self._fragments[element.name] = nfd

    def _on_fragment_definition_out(self, *_args, **_kwargs):
        self._internal_ctx.fragment_definition = None

    def _fragment_spread(self, ctx, element):
        _ctx = self._internal_ctx
        self._internal_ctx = ctx

        self._used_fragments.add(element.name)
        try:
            cfd = self._fragments[element.name]
        except KeyError:
            self._add_exception(
                UndefinedFragment(
                    "Undefined fragment < %s >." % element.name,
                    locations=[element.get_location()],
                )
            )
            return

        depth = self._internal_ctx.depth
        self._internal_ctx.type_condition = cfd.type_condition

        for saved_callback in cfd.callbacks:
            saved_callback(
                type_cond_depth=depth
            )  # Simulate calling a the right place.

        self._internal_ctx.type_condition = None
        self._internal_ctx = _ctx

    def _on_fragment_spread_out(
        self, element: _VisitorElement, *_args, **_kwargs
    ):
        self._to_call_later.append(
            partial(self._fragment_spread, self._internal_ctx.clone(), element)
        )

    def _on_operation_definition_in(
        self, element: _VisitorElementOperationDefinition, *_args, **_kwargs
    ):
        try:
            operation_node = self._named_operations[element.name]
        except KeyError:
            operation_node = NodeOperationDefinition(
                self._internal_ctx.path,
                element.get_location(),
                element.name,
                element.get_operation(),
            )
            if element.name is not None:
                self._named_operations[element.name] = operation_node
            else:
                self._anonymous_operations.append(operation_node)
        else:
            self._add_exception(
                NotUniqueOperationName(
                    "Operation name < %s > should be unique." % element.name,
                    locations=[
                        operation_node.location,
                        element.get_location(),
                    ],
                )
            )
            return

        self._internal_ctx.operation = operation_node

    def _on_operation_definition_out(self, *_args, **_kwargs):
        self._internal_ctx.operation = None

    def _on_inline_fragment_in(self, element, *_args, **_kwargs):
        a_type = element.get_named_type()
        self._internal_ctx.inline_fragment_info = InlineFragmentInfo(
            a_type, self._internal_ctx.depth
        )
        self._internal_ctx.type_condition = a_type

    def _on_inline_fragment_out(self, *_args, **_kwargs):
        self._internal_ctx.inline_fragment_info = None
        self._internal_ctx.type_condition = None

    def _on_document_out(self, *_args, **_kwargs):
        for saved_callback in self._to_call_later:
            saved_callback()

        unused_fragments = set(self._fragments) - self._used_fragments
        for unused_fragment in unused_fragments:
            self._add_exception(
                UnusedFragment(
                    "Fragment < %s > is never used." % unused_fragment,
                    locations=[self._fragments[unused_fragment].location],
                )
            )

        if self._anonymous_operations and (
            len(self._anonymous_operations) > 1 or self._named_operations
        ):
            for operation in self._anonymous_operations:
                self._add_exception(
                    NotLoneAnonymousOperation(
                        "Anonymous operation must be the only defined operation.",
                        locations=[operation.location],
                    )
                )

    def _on_selection_set_in(
        self, element: _VisitorElementSelectionSet, *_args, **_kwargs
    ):
        if (
            self._internal_ctx.operation.type == "Subscription"
            and self._internal_ctx.depth == 0
            and element.get_selections_size() > 1
        ):
            self._add_exception(
                MultipleRootNodeOnSubscriptionOperation(
                    "Subscription operations must have exactly one root field.",
                    locations=[self._internal_ctx.operation.location],
                )
            )

    def _in(self, element: _VisitorElement, *args, **kwargs):
        self._internal_ctx.move_in(element)

        try:
            self._events[self.IN][element.libgraphql_type](
                element, *args, **kwargs
            )
        except KeyError:
            pass

    def _out(self, element: _VisitorElement, *args, **kwargs):
        self._internal_ctx.move_out()

        try:
            self._events[self.OUT][element.libgraphql_type](
                element, *args, **kwargs
            )
        except KeyError:
            pass

    def update(self, event, element: _VisitorElement):
        self.continue_child = 1
        self.event = event

        if (
            not self._internal_ctx.fragment_definition
            or element.libgraphql_type == "FragmentDefinition"
        ):
            # Always execute FragmentDefinitions Handlers,
            # never exec if in fragment.
            self._events[self.event]["default"](element)
        else:
            self._internal_ctx.fragment_definition.callbacks.append(
                partial(self._events[self.event]["default"], element)
            )
