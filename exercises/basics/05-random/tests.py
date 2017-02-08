from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("probability_of_sum_higher_than"), all_or_nothing():
        probability_of_sum_higher_than = reftest(result=must_be_equal.with_epsilon(0.01))

        probability_of_sum_higher_than(1, 0, 1)
        probability_of_sum_higher_than(1, 7, 1)
        probability_of_sum_higher_than(5, 16, 10000)
        probability_of_sum_higher_than(5, 24, 10000)
        probability_of_sum_higher_than(5, 30, 10000)
