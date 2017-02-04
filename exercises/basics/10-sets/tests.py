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

    with tested_function_name("remove_duplicates"), all_or_nothing():
        remove_duplicates = reftest()
        
        remove_duplicates([])
        remove_duplicates([1])
        remove_duplicates([1, 1])
        remove_duplicates([1, 1, 1])
        remove_duplicates([1, 2, 1])
        remove_duplicates([2, 1, 2])
        remove_duplicates([1, 2, 3, 2, 1])
