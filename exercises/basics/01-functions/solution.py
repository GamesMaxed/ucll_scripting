def increment(x):
    return x + 1


def square(x):
    return x * x


def are_ordered(x, y, z):
    return (x <= y and y <= z) or (x >= y and y >= z)


def is_divisible_by(x, y):
    return y != 0 and x % y == 0
