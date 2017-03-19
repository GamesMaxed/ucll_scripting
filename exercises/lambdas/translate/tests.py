from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *



with cumulative(skip_after_fail=True):
    with tested_function_name('double_all'), all_or_nothing():
        double_all = reftest()

        double_all([])
        double_all([1])
        double_all([1, 2])
        double_all([1, 2, 3])
        double_all([1, 2, 3, 4])
        double_all([1, 1])
        double_all([0, 8, 100])

    with tested_function_name('square_all'), all_or_nothing():
        square_all = reftest()

        square_all([])
        square_all([1])
        square_all([1, 2])
        square_all([1, 2, 3])
        square_all([1, 2, 3, 4])
        square_all([1, 1])
        square_all([0, 8, 100])

    with tested_function_name('sum_of_squares'), all_or_nothing():
        sum_of_squares = reftest()

        sum_of_squares([])
        sum_of_squares([1])
        sum_of_squares([1, 2])
        sum_of_squares([1, 2, 3])
        sum_of_squares([1, 2, 3, 4])
        sum_of_squares([1, 1])
        sum_of_squares([0, 8, 100])
        
    with tested_function_name('select_odd'), all_or_nothing():
        select_odd = reftest()

        select_odd([])
        select_odd([1])
        select_odd([1, 2])
        select_odd([1, 2, 3])
        select_odd([1, 2, 3, 4])

    with tested_function_name('select_and_square_odd'), all_or_nothing():
        select_and_square_odd = reftest()

        select_and_square_odd([])
        select_and_square_odd([1])
        select_and_square_odd([1, 2])
        select_and_square_odd([1, 2, 3])
        select_and_square_odd([1, 2, 3, 4])
        select_and_square_odd([1, 1])
        select_and_square_odd([0, 8, 100])

    with tested_function_name('all_even'), all_or_nothing():
        all_even = reftest()

        all_even([])
        all_even([1])
        all_even([1, 2])
        all_even([1, 2, 3])
        all_even([1, 2, 3, 4])
        all_even([0, 2, 4])
        all_even([1, 1])
        all_even([0, 8, 100])
        
    with tested_function_name('all_in_range'), all_or_nothing():
        all_in_range = reftest()

        all_in_range([], 1, 10)
        all_in_range([1], 1, 10)
        all_in_range([1], 2, 10)
        all_in_range([1, 2], 1, 5)
        all_in_range([1, 2, 3], -5, 2)
        all_in_range([1, 2, 3, 4], 1, 10)
        all_in_range([0, 2, 4], 1, 100)
        all_in_range([1, 1], 1, 5)
        all_in_range([0, 8, 100], 1, 5)
        
    with tested_function_name('find_matching_strings'), all_or_nothing():
         find_matching_strings = reftest()

         find_matching_strings(['', 'a', 'b', 'ab'], r'[a-z]')
         find_matching_strings(['', 'a', 'b', 'ab', 'abc', '123'], r'[a-z]+')
         find_matching_strings(['', 'a', 'b', 'ab', 'abc', '123'], r'\d')

    with tested_function_name('minimum'), all_or_nothing():
         minimum = reftest()

         minimum([1])
         minimum([1, 2])
         minimum([1, 2, 3])
         minimum([3, 2, 1])
         minimum(['a', 'b', 'c'])
         minimum(['g', 'e', 'h', 'a', 'b'])
         
