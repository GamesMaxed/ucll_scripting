def inverse_lookup(xs):
    result = dict()

    for i in range(0, len(xs)):
        x = xs[i]

        if x not in result:
            result[x] = i

    return result


def get_with_default(map, key, default):
    if key in map:
        return map[key]
    else:
        return default

# Kortere oplossing (functionaliteit is reeds ingebouwd in Python dicts)
def get_with_default(map, key, default):
    return map.get(key, default)


def count_frequencies(xs):
    result = dict()

    for x in xs:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1

    return result
