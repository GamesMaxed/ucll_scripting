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
