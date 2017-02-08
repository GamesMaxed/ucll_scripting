from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("increment"), do_not_count():
        increment = reftest()

        for i in range(-10,10):
            increment(i)

    with tested_function_name("square"), all_or_nothing():
        square = reftest()

        for i in range(-10,10):
            square(i)

    with tested_function_name("are_ordered"), all_or_nothing():
        are_ordered = reftest()

        for x in [-4, 0, 5]:
            for y in [-1, 0, 7]:
                for z in [-5, 0, 3]:
                    are_ordered(x, y, z)
        
    with tested_function_name("is_divisible_by"), all_or_nothing():
        is_divisible_by = reftest()

        for x in [28, -4, 0, 5]:
            for y in [-1, 0, 5, 7, 10]:
                is_divisible_by(x, y)
        
