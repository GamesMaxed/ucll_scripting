from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing():
    def testcase(plaintext):
        morseCode = reference_module().encode_morse(plaintext)

        with tested_function_name("decode_morse"):
            @test("decode_morse({}) should return {}", repr(morseCode), repr(plaintext))
            def _():
                must_be_equal(plaintext, tested_function(morseCode))

        with tested_function_name("encode_morse"):
            @test("encode_morse({}) should return {}", repr(plaintext), repr(morseCode))
            def _():
                must_be_equal(morseCode, tested_function(plaintext))
            
    testcase('')

    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
        testcase(str(char))

    for plaintext in [ 'SOS', 'PYTHON', '12345' ]:
        testcase(plaintext)
