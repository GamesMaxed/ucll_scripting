from typing import List
from functools import reduce

def inverse_lookup(xs):
    result = dict()

    for i in range(0, len(xs)):
        x = xs[i]

        if x not in result:
            result[x] = i

    return result


def get_with_default(map: dict, key: str, default):
    if key in map:
        return map[key]
    else:
        return default


def count_frequencies(xs):
    result = dict()
    for x in xs:
        if x not in result:
            result[x] = 0
        result[x] += 1
    return result


def css_lookup(stylesheets: List[dict], key: str, default):
    for stylesheet in stylesheets:
        if key in stylesheet:
            return stylesheet[key]

    return default


def word_width(letter_widths: dict, word: str):
    """
    Rekent de breedte van een woord uit in pixels.
    Elke letter heeft een verschillende breedte.
    De breedte van elke letter staat gegeven in
    de dictionary letter_widths.
    De breedte van het woord is gelijk aan de
    som van de breedtes der letters.

    Bv. letter_widths = { 'a': 16, 'b': 16, 'i': 5, 'l': '6', 'w': 20, ... }
        word = 'walibi'
    geeft als resultaat
        20 + 16 + 6 + 5 + 16 + 5 = 68
    """
    return sum(map(lambda letter: letter_widths[letter], word))


def group_by_extension(filenames: List[str]):
    """
    Gegeven een lijst filenames waarvan de 3 laatste tekens
    de extensie vormen, groepeer de bestandsnamen per extensie
    in een dictionary.
    De keys in de dictionary zijn de extensies,
    de bijhorende waarde is een lijst van bestandsnamen
    met die extensie.
    
    Bv. [ 'foo.txt', 'bar.txt', 'baz.png' ]
    moet de dictionary
      { 'txt': [ 'foo.txt', 'bar'txt' ],
        'png': [ 'baz.png' ] }
    opleveren.
    """
    result = dict()

    for filename in filenames:
        extension = filename[-3:]

        if extension not in result:
            result[extension] = list()

        result[extension].append(filename)

    return result


