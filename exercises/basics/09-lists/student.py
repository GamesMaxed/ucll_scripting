# Importeert de math module (nodig voor math.inf)
import math


def sum(ns):
    total = 0

    for n in ns:
        total += n

    return total


def interval(a, b):
    raise NotImplementedError()


def maximum(ns):
    raise NotImplementedError()


def factors(n):
    raise NotImplementedError()


def remove_short_strings(strings, minimum_length):
    raise NotImplementedError()


def longest_increasing_subsequence(xs):
    """
    Zoekt de langste stijgende deelrij.

    Een deelrij is een reeks aaneensluitende elementen, m.a.w.
    men mag geen elementen overslaan.
    Bv. [2, 3, 4] is een deelrij van [1,2,3,4,5],
    maar niet [1, 3, 5].

    Een stijgende deelrij mag gelijke elementen bevatten:
    [1, 2, 2, 3] is stijgend.
    """
    
    raise NotImplementedError()
