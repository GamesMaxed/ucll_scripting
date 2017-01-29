from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name("sign"):
    check = reftest()

    for i in range(-10,10):
        check(i)
