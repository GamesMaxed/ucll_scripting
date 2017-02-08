def count(xs, predicate):
    count = 0

    for x in xs:
        if predicate(x):
            count += 1

    return count


def find_first(xs, predicate, default = None):
    for x in xs:
        if predicate(x):
            return x

    return default


def group_by_key(xs, key_function):
    result = {}

    for x in xs:
        key = key_function(x)

        if key not in result:
            result[key] = []

        result[key].append(x)

    return result
