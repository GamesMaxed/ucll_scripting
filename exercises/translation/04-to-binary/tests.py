from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing, testedFunctionName("toBinary"):
    check = reftest()

    for i in range(0,32):
        check(i)

    @test("toBinary(-4) should throw exception")
    def exceptionTest():
        mustRaise( RuntimeError, lambda: testedFunction(-4) )
