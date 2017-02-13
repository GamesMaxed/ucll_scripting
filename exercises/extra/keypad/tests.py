from testing import *
from testing.tests import *
from testing.assertions import *
from testing.conditions import *

import testing.conditions


with cumulative():
    with tested_function_name('corresponding_letters'), all_or_nothing():
        corresponding_letters = reftest()

        for i in range(2, 10):
            corresponding_letters(i)

    with tested_function_name('find_words'), all_or_nothing():
        find_words = reftest()

        find_words([], [])
        find_words([], [2])
        find_words(['a'], [2])
        find_words(['b'], [2])
        find_words(['c'], [2])
        find_words(['a', 'b', 'c'], [2])
        find_words(['a', 'b', 'c'], [2, 2])
        find_words(['aa', 'ba', 'ca'], [2, 2])
        find_words(['aa', 'bb', 'cc'], [2, 2])
        find_words(['ac', 'ba', 'cb', 'ad'], [2, 2])
        find_words(['cat', 'dog', 'rat', 'aa'], [2, 2, 8])

        words = reference_module().read_words()

        find_words(words, [2, 3, 4])
        find_words(words, [2, 3, 3])
        find_words(words, [7, 2, 4, 6, 8, 3, 7])
        find_words(words, [8, 5, 8, 5, 3, 5, 3])
