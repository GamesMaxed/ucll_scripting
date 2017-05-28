'''
Onderstaande code steunt op lussen. Herschrijf het
zodat het gebruik maakt van hulpfuncties,
list comprehensions, lambda's, ...

Merk op dat de tests meteen slagen omdat je reeds
werkende implementaties hebt gekregen. Gebruik de tests
om na te gaan of je vertaling nog steeds correct is.
'''

import re

def double_all(ns):
    return [2 * n for n in ns]


def square_all(ns):
    return [n ** 2 for n in ns]


def sum_of_squares(ns):
    return sum(square_all(ns))


def select_odd(ns):
    return [n for n in ns if n % 2 == 1]
    

def select_and_square_odd(ns):
    return [n ** 2 for n in ns if n % 2 == 1]


# Zoek naar 'ternary if'
def square_odd(ns):
    return [n if n % 2 == 0 else n ** 2 for n in ns]


def all_even(ns):
    return all(n % 2 == 0 for n in ns)


def all_in_range(ns, min, max):
    return all(min <= n <= max for n in ns)


def find_matching_strings(strings, regex):
    return [string for string in strings if re.fullmatch(regex, string)]


def minimum(ns):
    return min(ns + [float('inf')])


def shortest(xs):
    return min(xs, key=lambda x: len(x))


def longest(xs):
    return max(xs, key=lambda x: len(x))


def is_prime(n):
    return n >= 2 and all(n % k != 0 for k in range(2, n))


def primes_up_to(n):
    return [k for k in range(0, n + 1) if is_prime(k)]


def zero_matrix(nrows, ncols):
    return [[0] * ncols for _ in range(nrows)]

def matrix(nrows, ncols, function):
    return [[function(row, col) for col in range(ncols)] for row in range(nrows)]

# Maak gebruik van matrix
def identity_matrix(size):
    return matrix(size, size, lambda row, col: 1 if row == col else 0)


def sum_of_2_lists(xs, ys):
    return [x + y for x, y in zip(xs, ys)]


def sum_of_n_lists(xss):
    return [sum(xs) for xs in zip(*xss)]


# Uitdaging
def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


# Hulpfunctie; hoeft niet vertaald te worden
def matrix_row(a, row):
    return a[row]


# Deze wel vertalen
def matrix_column(a, col):
    return [a[row][col] for row in range(len(a))]


# Uitdaging
def matrix_product(a, b):
    return [[sum(a[row][k] * b[k][col] for k in range(len(b))) for col in range(0, len(b[0]))] for row in range(0, len(a))]