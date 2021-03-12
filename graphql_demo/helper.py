from graphql.utils.ast_to_dict import ast_to_dict


def collect_fields(node):
    fields = {}

    if node.get("selection_set"):
        for leaf in node["selection_set"]["selections"]:
            if leaf["kind"] == "Field":
                fields.update({leaf["name"]["value"]: collect_fields(leaf)})

    return fields


def get_fields(info):
    if not info.field_asts:
        return {}

    node = ast_to_dict(info.field_asts[0])

    return collect_fields(node)