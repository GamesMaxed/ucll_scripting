from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing(), testedFunctionName("sign"):
    check = reftest()

    for i in range(-10,10):
        check(i)
