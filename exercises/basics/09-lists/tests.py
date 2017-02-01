from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("sum"), all_or_nothing():
        sum = reftest()

        sum([])
        sum([0])
        sum([1])
        sum([1,2,3])
        sum([1,2,3,4,5,6])
        sum([5,1,4,7,4])

    with tested_function_name("maximum"), all_or_nothing():
        maximum = reftest()

        maximum([])
        maximum([0])
        maximum([1])
        maximum([1,2,3])
        maximum([1,2,3,4,5,6])
        maximum([5,1,4,7,4])

    with tested_function_name("factors"), all_or_nothing():
        factors = reftest()

        factors(1)
        factors(5)
        factors(10)
        factors(2400)
        factors(-3600)
        factors(17 * 19 * 31)

    with tested_function_name("remove_short_strings"), all_or_nothing():
        remove_short_strings = reftest(arguments=must_be_equal)

        remove_short_strings([], 4)
        remove_short_strings(['a'], 4)

        for n in range(0, 11):
            remove_short_strings( [ 'x' * k for k in range(0, 10) ], n )

