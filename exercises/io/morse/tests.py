from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing():
    def testcase(plaintext):
        morseCode = referenceModule().encodeMorse(plaintext)

        with testedFunctionName("decodeMorse"):
            @test("decodeMorse({}) should return {}", repr(morseCode), repr(plaintext))
            def _():
                must_be_equal(plaintext, testedFunction(morseCode))

        with testedFunctionName("encodeMorse"):
            @test("encodeMorse({}) should return {}", repr(plaintext), repr(morseCode))
            def _():
                must_be_equal(morseCode, testedFunction(plaintext))
            
    testcase('')

    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
        testcase(str(char))

    for plaintext in [ 'SOS', 'PYTHON', '12345' ]:
        testcase(plaintext)
