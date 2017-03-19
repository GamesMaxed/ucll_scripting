import re


def double_all(ns):
    return [ 2 * n for n in ns ]


def square_all(ns):
    return [ n**2 for n in ns ]


def sum_of_squares(ns):
    return sum( n**2 for n in ns )

def select_odd(ns):
    return [ n for n in ns if n % 2 == 1 ]


def select_and_square_odd(ns):
    return [ n**2 for n in ns if n % 2 == 1 ]


def square_odd(ns):
    return [ n**2 if n % 2 == 1 else n for n in ns ]


def all_even(ns):
    return all( n % 2 == 0 for n in ns )


def all_in_range(ns, min, max):
    return all( min <= n and n <= max for n in ns )


def find_matching_strings(strings, regex):
    return [ string for string in strings if re.fullmatch(regex, string) ]


def minimum(ns):
    return min(ns + [float('inf')])


def shortest(ns):
    return min(ns, key=lambda x: len(x))


def longest(ns):
    return max(ns, key=lambda x: len(x))


def is_prime(n):
    return n >= 2 and all( n % k != 0 for k in range(2, n) )


def primes_up_to(n):
    return [ k for k in range(0, n+1) if is_prime(k) ]


def zero_matrix(nrows, ncols):
    return [ [0] * ncols ] * nrows


def matrix(nrows, ncols, function):
    return [ [ function(row, col) for col in range(0, ncols) ] for row in range(0, nrows) ]


def identity_matrix(size):
    return matrix(size, size, lambda y, x: 1 if x == y else 0)
