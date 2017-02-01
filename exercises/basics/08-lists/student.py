# Importeert de math module (nodig voor math.inf)
import math


def sum(ns):
    total = 0

    for n in ns:
        total += n

    return total


def maximum(ns):
    raise NotImplementedError()


def factors(n):
    raise NotImplementedError()


def remove_short_strings(strings, minimum_length):
    return None
