from typing import Dict, List, Optional

from tartiflette.types.field import GraphQLField
from tartiflette.types.type import GraphQLType


class GraphQLObjectType(GraphQLType):
    """
    Object Type Definition

    Almost all of the GraphQL types you define will be object types.
    Object types are composite types and have a name,
    but most importantly describe their fields.
    """

    def __init__(
        self,
        name: str,
        fields: Dict[str, GraphQLField],
        interfaces: Optional[List[str]] = None,
        description: Optional[str] = None,
        schema=None,
    ):
        super().__init__(name=name, description=description, schema=schema)
        self._fields: Dict[str, GraphQLField] = fields
        # TODO: specify what is in the List.
        self.interfaces_names: Optional[List[str]] = interfaces or []
        self._interfaces = None

    def __repr__(self) -> str:
        return (
            "{}(name={!r}, fields={!r}, "
            "interfaces={!r}, description={!r})".format(
                self.__class__.__name__,
                self.name,
                self._fields,
                self.interfaces_names,
                self.description,
            )
        )

    def __eq__(self, other) -> bool:
        return (
            super().__eq__(other)
            and self._fields == other._fields
            and self.interfaces_names == other.interfaces_names
        )

    def add_field(self, value: GraphQLField):
        self._fields[value.name] = value

    def find_field(self, name: str) -> GraphQLField:
        return self._fields[name]

    # Introspection Attribute
    @property
    def kind(self):
        return "OBJECT"

    # Introspection Attribute
    @property
    def fields(self):
        try:
            return [x for _, x in self._fields.items()]
        except AttributeError:
            return []

    def bake(self, schema, custom_default_resolver):
        super().bake(schema, custom_default_resolver)
        self._interfaces = [
            self._schema.find_type(x) for x in self.interfaces_names
        ]

        for iface in self._interfaces:
            iface.possibleTypes.append(self)

        for field in self.fields:
            try:
                field.bake(schema, self, custom_default_resolver)
            except AttributeError:
                pass

    # Introspection Attribute
    @property
    def interfaces(self):
        return self._interfaces or []
