from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("create_interval"), all_or_nothing():
        create_interval = reftest()

        create_interval(0, 0)
        create_interval(0, 10)
        create_interval(4, 12)
        create_interval(9, 5)

    with tested_function_name("remove_duplicates_preserving_order"), all_or_nothing():
        remove_duplicates_preserving_order = reftest()
        
        remove_duplicates_preserving_order([])
        remove_duplicates_preserving_order(['a'])
        remove_duplicates_preserving_order(['a', 'b'])
        remove_duplicates_preserving_order(['a', 'a', 'a'])
        remove_duplicates_preserving_order(['a', 'a', 'a'])
        remove_duplicates_preserving_order(['c', 'b', 'a'])
        remove_duplicates_preserving_order([1, 2, 1])
        remove_duplicates_preserving_order([2, 1, 2])
        remove_duplicates_preserving_order([1, 2, 3, 2, 1])
        remove_duplicates_preserving_order([5, 7, 2, 3, 5, 7, 3])

    with tested_function_name("remove_duplicates_not_preserving_order"), all_or_nothing():
        remove_duplicates_not_preserving_order = reftest()
        
        remove_duplicates_not_preserving_order([])
        remove_duplicates_not_preserving_order(['a'])
        remove_duplicates_not_preserving_order(['a', 'b'])
        remove_duplicates_not_preserving_order(['a', 'a', 'a'])
        remove_duplicates_not_preserving_order(['c', 'b', 'a'])
        remove_duplicates_not_preserving_order([1, 2, 1])
        remove_duplicates_not_preserving_order([2, 1, 2])
        remove_duplicates_not_preserving_order([1, 2, 3, 2, 1])
        remove_duplicates_not_preserving_order([5, 7, 2, 3, 5, 7, 3])
        
    with tested_function_name("count_unique"), all_or_nothing():
        count_unique = reftest()

        count_unique( [] )
        count_unique( [1] )
        count_unique( [1, 1] )
        count_unique( [1, 2] )
        count_unique( [1, 2, 3, 4, 5] )
        count_unique( [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] )
