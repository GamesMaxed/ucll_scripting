def inverse_lookup(xs):
    result = dict()

    for i in range(0, len(xs)):
        x = xs[i]

        if x not in result:
            result[x] = i

    return result


def get_with_default(map, key, default):
    raise NotImplementedError()


def count_frequencies(xs):
    raise NotImplementedError()


# css_lookup
