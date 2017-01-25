from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing(), testedFunctionName("square"):
    check = reftest()

    for i in range(-10,10):
        check(i)
