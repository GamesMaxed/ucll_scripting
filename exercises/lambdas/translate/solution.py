def double_all(ns):
    return [ 2 * n for n in ns ]


def square_all(ns):
    return [ n**2 for n in ns ]


def select_odd(ns):
    return [ n for n in ns if n % 2 == 1 ]


def select_and_square_odd(ns):
    return [ n**2 for n in ns if n % 2 == 1 ]


def square_odd(ns):
    return [ n**2 if n % 2 == 1 else n for n in ns ]


def all_even(ns):
    return all( n % 2 == 0 for n in ns )


