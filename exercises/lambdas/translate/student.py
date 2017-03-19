'''
Onderstaande code steunt op lussen. Herschrijf het
zodat het gebruik maakt van hulpfuncties,
list comprehensions, lambda's, ...
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
    result = ns[0]

    for n in ns[1:]:
        if n < result:
            result = n

    return result

# max, min, sorted, any, find
