# Importeert de math module (nodig voor math.inf)
import math
from typing import List


def sum(ns: List[int]):
    total = 0

    for n in ns:
        total += n

    return total


def interval(a, b) -> List[int]:
    return list(range(a, b + 1))


def maximum(ns) -> int:
    result = -math.inf

    for i in ns:
        result = max(result, i)

    return result


def factors(n) -> List[int]:
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


def remove_short_strings(strings: List[str], minimum_length: int):
    for i in range(len(strings), 0, -1):
        j = i - 1
        if len(strings[j]) < minimum_length:
            del strings[j]


def longest_increasing_subsequence(xs: List[int]):
    """
    Zoekt de langste stijgende deelrij.

    Een deelrij is een reeks aaneensluitende elementen, m.a.w.
    men mag geen elementen overslaan.
    Bv. [2, 3, 4] is een deelrij van [1,2,3,4,5],
    maar niet [1, 3, 5].

    Een stijgende deelrij mag gelijke elementen bevatten:
    [1, 2, 2, 3] is stijgend.
    """
    if len(xs) == 0:
        return list()

    longest = list()
    current = list()
    last = math.inf

    for x in xs:
        if x < last:
            current = []

        current.append(x)

        if len(current) > len(longest):
            longest = current

        last = x

    return longest


def largest_difference(ns: List[int]) -> int:
    """
    Gegeven een lijst getallen ns,
    rekent het grootste verschil tussen 2 elementen uit ns.

    Bijvoorbeeld, ns = [5, 1, 2, 6, 8].
    5 en 1 verschillen 4 van elkaar.
    5 en 2 verschillen 3 van elkaar.
    etc.
    1 en 8 verschillen het meest van elkaar: 7. Dit is het resultaat.
    """
    return max(ns) - min(ns)


def group(xs, n_groups):
    """
    Gegeven een lijst xs en een geheel getal n_groups > 0,
    verdeel xs in n_groups groepen.
    * Groepen mogen niet overlappen.
    * Elk element uit xs moet voorkomen in een groep.
    * De elementen moeten gelijkmatig verdeeld zijn:
      de groepen mogen maximum 1 element van elkaar verschillen
      in grootte.

    Bijvoorbeeld, [1, 2, 3, 4, 5, 6] verdelen in 3 groepen kan
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
    result = list(list() for _ in range(0, n_groups))

    for i, x in enumerate(xs):
        result[i % n_groups].append(x)

    return result
