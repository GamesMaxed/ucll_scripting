from testing import *
from testing.tests import *
from testing.assertions import *

with cumulative():
    with tested_function_name('count'), all_or_nothing():
        count = reftest()

        def alwaysTrue(x):
            return True

        def alwaysFalse(x):
            return False

        def isOdd(x):
            return x % 2 != 0

        def isInt(x):
            return type(x) == int

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
