from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("sign"), all_or_nothing():
        sign = reftest()

        for i in range(-10,10):
            sign(i)

    with tested_function_name("factorial"), all_or_nothing():
        factorial = reftest()

        for i in range(-10,10):
            factorial(i)
