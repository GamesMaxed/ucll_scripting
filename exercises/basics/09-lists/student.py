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


def largest_difference(ns):
    """
    Gegeven een lijst getallen ns,
    rekent het grootste verschil tussen 2 elementen uit ns.

    Bijvoorbeeld, ns = [5, 1, 2, 6, 8].
    5 en 1 verschillen 4 van elkaar.
    5 en 2 verschillen 3 van elkaar.
    etc.
    1 en 8 verschillen het meest van elkaar: 7. Dit is het resultaat.
    """
    raise NotImplementedError()


def group(xs, n_groups):
    """
    Gegeven een lijst xs en een geheel getal n_groups > 0,
    verdeel xs in n_groups groepen.
    * Groepen mogen niet overlappen.
    * Elk element uit xs moet voorkomen in een groep.
    * De elementen moeten gelijkmatig verdeeld zijn:
      de groepen mogen maximum 1 element van elkaar verschillen
      in grootte.

    Bijvoorbeeld, [1, 2, 3, 5, 6] verdelen in 3 groepen kan
    als volgt:
      [ [1, 2], [3, 4], [5, 6] ]
      [ [1, 4], [2, 6], [3, 5] ]
      etc.
    Elke groepering die voldoet aan de regels is ok. Er zijn
    dus veel mogelijke groeperingen.
      [ [1, 2, 3], [4, 5], [6] ]
    is geen geldige groepering, omdat het verschil
    in grootte tussen de eerste en laatste groep te groot is,
    m.a.w. de elementen zijn niet gelijkmatig verdeeld.
    """
    raise NotImplementedError()
