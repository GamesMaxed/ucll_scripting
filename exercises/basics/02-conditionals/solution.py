def abs(x):
    if x < 0:
        return -x
    else:
        return x


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def are_ordered(x, y, z):
    return (x <= y and y <= z) or (x >= y and y >= z)
