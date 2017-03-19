from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *



with cumulative(skip_after_fail=True):
    with tested_function_name('double_list'), all_or_nothing():
        double_list = reftest()

        double_list([])
        double_list([1])
        double_list([1, 2])
        double_list([1, 2, 3])
        double_list([1, 2, 3, 4])
        double_list([1, 1])
        double_list([0, 8, 100])

    with tested_function_name('square_list'), all_or_nothing():
        square_list = reftest()

        square_list([])
        square_list([1])
        square_list([1, 2])
        square_list([1, 2, 3])
        square_list([1, 2, 3, 4])
        square_list([1, 1])
        square_list([0, 8, 100])
