from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name("sum_up_to"):
    check = reftest()

    for i in range(0,10):
        check(i)
