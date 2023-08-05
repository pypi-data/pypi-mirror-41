from functools import partial

from tartiflette.types.argument import GraphQLArgument
from tartiflette.types.field import GraphQLField
from tartiflette.types.helpers import get_typename
from tartiflette.types.non_null import GraphQLNonNull


async def __schema_resolver(_pr, _arg, _rctx, info):
    info.execution_ctx.is_introspection = True
    return info.schema


async def __type_resolver(_pr, args, _rctx, info):
    info.execution_ctx.is_introspection = True
    return info.schema.find_type(args["name"])


SCHEMA_ROOT_FIELD_DEFINITION = partial(
    GraphQLField,
    name="__schema",
    description="Access the current type schema of this server.",
    arguments={},
    resolver=__schema_resolver,
)


def prepare_type_root_field(schema):
    return GraphQLField(
        name="__type",
        description="Request the type information of a single type.",
        arguments={
            "name": GraphQLArgument(
                name="name",
                gql_type=GraphQLNonNull("String", schema=schema),
                schema=schema,
            )
        },
        gql_type="__Type",
        resolver=__type_resolver,
        schema=schema,
    )


async def __typename_resolver(parent_result, _args, _req_ctx, info):
    tn_pr = get_typename(parent_result)

    try:
        return info.schema_field.schema.find_type(tn_pr)
    except (AttributeError, KeyError):
        pass

    return info.schema_field.parent_type


TYPENAME_ROOT_FIELD_DEFINITION = partial(
    GraphQLField,
    name="__typename",
    description="The name of the current Object type at runtime.",
    arguments={},
    resolver=__typename_resolver,
)
