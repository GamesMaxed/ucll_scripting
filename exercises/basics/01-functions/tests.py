from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("square"), all_or_nothing():
        check = reftest()

        for i in range(-10,10):
            check(i)

    with tested_function_name("are_ordered"), all_or_nothing():
        are_ordered = reftest()

        for x in [-4, 0, 5]:
            for y in [-1, 0, 7]:
                for z in [-5, 0, 3]:
                    are_ordered(x, y, z)
        
