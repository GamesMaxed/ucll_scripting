from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing(), testedFunctionName("monotone"):
    check = reftest()

    for x in [-100, -4, 6, 14, 100]:
        for y in [-100, -2, 6, 19, 100]:
            for z in [-100, -5, 6, 33, 100]:
                check(x, y, z)
