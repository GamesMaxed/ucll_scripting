def create_interval(a, b):
    result = set()

    for i in range(a, b + 1):
        result.add(i)

    return result

# Kortere implementatie
def create_interval(a, b):
    return set( range(a, b+1) )


def remove_duplicates_preserving_order(strings):
    found = set()
    result = []

    for string in strings:
        if string not in found:
            result.append(string)
            found.add(string)

    return result


def remove_duplicates_not_preserving_order(strings):
    return list(set(strings))


def count_unique(ns):
    return len(set(ns))
