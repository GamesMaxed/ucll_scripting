def get_fields(objects, field_name):
    result = []

    for o in objects:
        result.append(getattr(o, field_name))

    return result
