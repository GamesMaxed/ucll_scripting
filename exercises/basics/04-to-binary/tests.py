from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name("to_binary"):
    check = reftest()

    for i in range(0,32):
        check(i)

    @test("to_binary(-4) should throw exception")
    def _():
        must_raise( RuntimeError, lambda: tested_function(-4) )
