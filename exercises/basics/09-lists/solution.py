# Importeert de math module (nodig voor math.inf)
import math


def sum(ns):
    total = 0

    for n in ns:
        total += n

    return total


def interval(a, b):
    result = []

    for i in range(a, b + 1):
        result.append(i)

    return result


# Kortere oplossing
def interval(a, b):
    return list(range(a, b+1))


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


def remove_short_strings(strings, minimum_length):
    for i in range(len(strings), 0, -1):
        j = i-1
        if len(strings[j]) < minimum_length:
            del strings[j]


def longest_increasing_subsequence(xs):
    if len(xs) == 0:
        return []
    else:
        longest = []
        current = []
        last = math.inf
    
        for x in xs:
            if x < last:
                current = []
                
            current.append(x)

            if len(current) > len(longest):
                longest = current

            last = x

        return longest
