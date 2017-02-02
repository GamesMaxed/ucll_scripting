def contains(lst, x):
    # Elk element om beurt afgaan
    for y in lst:
        if x == y:
            return True

    return False
