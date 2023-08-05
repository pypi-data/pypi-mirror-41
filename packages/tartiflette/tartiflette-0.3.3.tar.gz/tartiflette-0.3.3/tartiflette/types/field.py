from typing import Dict, Optional

from tartiflette.resolver import ResolverExecutorFactory
from tartiflette.types.helpers import get_directive_implem_list
from tartiflette.types.type import GraphQLType


class GraphQLField:
    """
    Field Definition

    A field is used in Object, Interfaces as its constituents.
    """

    def __init__(
        self,
        name: str,
        gql_type: str,
        arguments: Optional[Dict] = None,
        resolver: Optional[callable] = None,
        description: Optional[str] = None,
        directives: Optional[Dict] = None,
        schema: Optional = None,
    ):
        self.name = name
        self.gql_type = gql_type
        self.arguments = arguments if arguments else {}

        self._directives = directives
        self._schema = schema
        self.description = description if description else ""

        self.resolver = ResolverExecutorFactory.get_resolver_executor(
            resolver, self
        )
        self.parent_type = None

        # Introspection Attribute
        self.isDeprecated = False  # pylint: disable=invalid-name
        self._directives_implementations = None

    def __repr__(self):
        return (
            "{}(name={!r}, gql_type={!r}, arguments={!r}, "
            "resolver={!r}, description={!r}, directives={!r})".format(
                self.__class__.__name__,
                self.name,
                self.gql_type,
                self.arguments,
                self.resolver,
                self.description,
                self.directives,
            )
        )

    @property
    def directives(self):
        return self._directives_implementations

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self is other or (
            type(self) is type(other)
            and self.name == other.name
            and self.gql_type == other.gql_type
            and self.arguments == other.arguments
            and self.resolver == other.resolver
            and self.directives == other.directives
        )

    # Introspection Attribute
    @property
    def kind(self):
        try:
            return self.gql_type.kind
        except AttributeError:
            return "FIELD"

    # Introspection Attribute
    @property
    def type(self):
        if isinstance(self.gql_type, GraphQLType):
            return self.gql_type

        return self.schema.find_type(self.gql_type)

    # Introspection Attribute
    @property
    def args(self):
        return [x for _, x in self.arguments.items()]

    @property
    def schema(self):
        return self._schema

    def bake(self, schema, parent_type, custom_default_resolver):
        self._schema = schema
        self._directives_implementations = get_directive_implem_list(
            self._directives, self._schema
        )
        self.resolver.bake(custom_default_resolver)
        self.parent_type = parent_type

        for arg in self.arguments.values():
            arg.bake(self._schema)

    def get_arguments_default_values(self):
        # return a new instance each call cause we don't want caller to modify ours.
        return {
            key: val.default_value
            for key, val in self.arguments.items()
            if val.default_value
        }
