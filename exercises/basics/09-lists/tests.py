from testing import *
from testing.tests import *
from testing.assertions import *
import sys


with cumulative():
    with tested_function_name("sum"), do_not_count():
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

    with tested_function_name("longest_increasing_subsequence"), all_or_nothing():
        longest_increasing_subsequence = reftest()

        longest_increasing_subsequence([])
        longest_increasing_subsequence([0])
        longest_increasing_subsequence([0,1,2,3,4,5])
        longest_increasing_subsequence([5,1,2,3,0])
        longest_increasing_subsequence([1,2,3,2,3,4])
        longest_increasing_subsequence([1,5,2,6,3,7,4,8,5,9])
        longest_increasing_subsequence([1,3,5,7,9,2,4,6,8])
        longest_increasing_subsequence([1,3,5,7,9,2,4,6,8,10,12])
        longest_increasing_subsequence([50,55,58,40,41,42,43,45,48,49,10,15,18])

    with tested_function_name("largest_difference"), all_or_nothing():
        largest_difference = reftest()

        largest_difference([0])
        largest_difference([1, 1])
        largest_difference([1, 2, 3])
        largest_difference([4, 2, 1, 6, 8])
        largest_difference([2, 2, 1, 6, 1, 8])

    with tested_function_name("group"), all_or_nothing():
        def check(xs, n):
            def largest_difference(ns):
                return max(ns) - min(ns)


            if len(set(xs)) != len(xs):
                sys.exit('Invalid test case; elements should be unique')
            
            @test("group({}, {})", xs, n)
            def _():
                result = tested_function(xs, n)
                flattened_results = [ x for group in result for x in group ]

                with context('expected {} groups', n):
                    must_be_equal(n, len(result))
                
                with context('each element must appear in some group'):
                    must_be_equal( set(xs), set(flattened_results) )

                with context('group size must differ at most by one'):
                    must_be_element( {0, 1}, largest_difference( [ len(group) for group in result ] ) )


        for n in range(0, 10):
            for k in range(1, 6):
                check( list(range(0, n)), k )
