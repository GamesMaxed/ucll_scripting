# Importeert de math module (nodig voor math.inf)
import math


def sum(ns):
    total = 0

    for n in ns:
        total += n

    return total


def maximum(ns):
    result = -math.inf

    for n in ns:
        result = max(result, n)

    return result


def factors(n):
    result = []

    n = abs(n)
    
    k = 2
    while n > 1:
        if n % k == 0:
            result.append(k)
            n /= k
        else:
            k += 1

    return result
