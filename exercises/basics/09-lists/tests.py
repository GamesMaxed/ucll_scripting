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

    with tested_function_name('interval'), all_or_nothing():
        interval = reftest()

        interval(0, 0)
        interval(0, 5)
        interval(2, 5)
        interval(10, 0)

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

    with all_or_nothing(), tested_function_name("longest_increasing_subsequence"):
        check = reftest()

        check([])
        check([0])
        check([0,1,2,3,4,5])
        check([5,1,2,3,0])
        check([1,2,3,2,3,4])
        check([1,5,2,6,3,7,4,8,5,9])
        check([1,3,5,7,9,2,4,6,8])
        check([1,3,5,7,9,2,4,6,8,10,12])
        check([50,55,58,40,41,42,43,45,48,49,10,15,18])
