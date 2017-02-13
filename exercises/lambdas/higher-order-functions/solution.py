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


def filter(xs, predicate):
    return [ x for x in xs if predicate(x) ]


def all(xs, predicate):
    for x in xs:
        if not predicate(x):
            return False

    return True


def any(xs, predicate):
    for x in xs:
        if predicate(x):
            return True

    return False


def group_by_key(xs, key_function):
    result = {}

    for x in xs:
        key = key_function(x)

        if key not in result:
            result[key] = []

        result[key].append(x)

    return result


def memoize(function):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]
        else:
            result = function(x)
            cache[x] = result
            return result

    return wrapper


def create_change_detector():
    last = None
    is_first = True

    def function(x):
        nonlocal last
        nonlocal is_first

        if is_first or x != last:
            is_first = False
            last = x
            return True
        else:
            return False

    return function
