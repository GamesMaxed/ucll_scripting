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
    result = []

    for n in ns:
        result.append(2 * n)

    return result


def square_all(ns):
    result = []

    for n in ns:
        result.append(n ** 2)

    return result


def sum_of_squares(ns):
    result = 0

    for n in ns:
        result += n ** 2

    return result


def select_odd(ns):
    result = []

    for n in ns:
        if n % 2 == 1:
            result.append(n)

    return result
    

def select_and_square_odd(ns):
    result = []

    for n in ns:
        if n % 2 == 1:
            result.append(n ** 2)

    return result


# Zoek naar 'ternary if'
def square_odd(ns):
    result = []

    for n in ns:
        if n % 2 == 1:
            result.append(n ** 2)
        else:
            result.append(n)

    return result


def all_even(ns):
    for n in ns:
        if n % 2 == 1:
            return False

    return True


def all_in_range(ns, min, max):
    for n in ns:
        if n < min or n > max:
            return False

    return True


def find_matching_strings(strings, regex):
    result = []

    for string in strings:
        if re.fullmatch(regex, string):
            result.append(string)

    return result


def minimum(ns):
    result = float('inf')

    for n in ns:
        if n < result:
            result = n

    return result


def shortest(xs):
    result = xs[0]

    for x in xs[1:]:
        if len(x) < len(result):
            result = x

    return result


def longest(xs):
    result = xs[0]

    for x in xs[1:]:
        if len(x) > len(result):
            result = x

    return result


def is_prime(n):
    for k in range(2, n):
        if n % k == 0:
            return False

    return n >= 2


def primes_up_to(n):
    result = []
    
    for k in range(0, n+1):
        if is_prime(k):
            result.append(k)

    return result


def zero_matrix(nrows, ncols):
    result = []

    for i in range(0, nrows):
        row = []

        for j in range(0, ncols):
            row.append(0)

        result.append(row)

    return result


def matrix(nrows, ncols, function):
    result = []

    for row in range(0, nrows):
        acc = []

        for col in range(0, ncols):
            acc.append(function(row, col))

        result.append(acc)

    return result


# Maak gebruik van matrix
def identity_matrix(size):
    result = []

    for row in range(0, size):
        acc = []
        
        for col in range(0, size):
            if row == col:
                acc.append(1)
            else:
                acc.append(0)

        result.append(acc)

    return result


def sum_of_2_lists(xs, ys):
    result = []

    for i in range(0, min(len(xs), len(ys))):
        result.append(xs[i] + ys[i])

    return result


# Uitdaging
def transpose(matrix):
    result = []

    nrows = len(matrix[0])
    ncols = len(matrix)

    for row in range(0, nrows):
        acc = []

        for col in range(0, ncols):
            acc.append(matrix[col][row])

        result.append(acc)

    return result


# max, sorted, any, find
