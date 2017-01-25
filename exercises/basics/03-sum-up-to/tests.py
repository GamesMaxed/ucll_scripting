from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing(), testedFunctionName("sumUpTo"):
    check = reftest()

    for i in range(0,10):
        check(i)
