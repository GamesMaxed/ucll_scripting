def double_all(ns):
    return [ 2 * n for n in ns ]


def square_all(ns):
    return [ n**2 for n in ns ]


def select_odd(ns):
    return [ n for n in ns if n % 2 == 1 ]


def select_and_square_odd(ns):
    return [ n**2 for n in ns if n % 2 == 1 ]

