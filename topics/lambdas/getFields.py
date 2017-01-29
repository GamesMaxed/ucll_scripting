def get_fields(objects, fieldName):
    result = []

    for o in objects:
        result.append(getattr(o, fieldName))

    return result
