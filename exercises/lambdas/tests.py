from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *


with cumulative():
    alwaysTrue = named_lambda('alwaysTrue', lambda x: True)
    alwaysFalse = named_lambda('alwaysFalse', lambda x: False)
    isOdd = named_lambda('isOdd', lambda x: x % 2 != 0)
    isInt = named_lambda('isOdd', lambda x: type(x) == int)


    with tested_function_name('count'), all_or_nothing():
        count = reftest()

        count([], alwaysTrue)
        count([1], alwaysTrue)
        count([1, 2, 3], alwaysTrue)
        count([], alwaysFalse)
        count([1], alwaysFalse)
        count([1, 2, 3], alwaysFalse)
        count([1, 2, 3], isOdd)
        count([1, 2, 3, 4, 5], isOdd)
        count([1, 2, 3, 4, 5], isInt)
        count(['x', 1, '4', 2], isInt)

    with tested_function_name('find_first'), all_or_nothing():
        find_first = reftest()

        find_first([], alwaysTrue, 1)
        find_first([], alwaysTrue, None)
        find_first([], alwaysTrue, 'default')
        find_first([1], alwaysTrue, 1)
        find_first([1, 2], alwaysTrue, 1)
        find_first([1, 2, 3], alwaysTrue, 1)
        find_first([1], alwaysFalse, 7)
        find_first([1, 2], alwaysFalse, 4)
        find_first([1, 2, 3], alwaysFalse, 99)
