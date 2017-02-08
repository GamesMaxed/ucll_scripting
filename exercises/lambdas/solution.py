def count(xs, predicate):
    count = 0

    for x in xs:
        if predicate(x):
            count += 1

    return count


