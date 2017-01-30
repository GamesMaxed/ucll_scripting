from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("to_binary"), all_or_nothing():
        to_binary = reftest()

        for i in range(0,32):
            to_binary(i)

        @test("to_binary(-4) should throw exception")
        def _():
            must_raise( RuntimeError, lambda: tested_function(-4) )

    with tested_function_name("from_binary"), all_or_nothing():
        from_binary = reftest()

        for string in [ '0', '1', '10', '11', '101010', '111111', '000000' ]:
            from_binary(string)

        @test("from_binary('151') should throw exception")
        def _():
            must_raise( RuntimeError, lambda: tested_function('151') )
            
