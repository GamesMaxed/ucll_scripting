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


def factorial(n):
    if n < 0:
        return -factorial(-n)
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
