from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative:
    def testcase(plaintext):
        morseCode = referenceModule().encodeMorse(plaintext)

        with testedFunctionName("decodeMorse"):
            @test("decodeMorse({}) should return {}", repr(morseCode), repr(plaintext))
            def testFunction():
                mustBeEqual(plaintext, testedFunction(morseCode))

        with testedFunctionName("encodeMorse"):
            @test("encodeMorse({}) should return {}", repr(plaintext), repr(morseCode))
            def testFunction():
                mustBeEqual(morseCode, testedFunction(plaintext))
            
    testcase('')

    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
        testcase(str(char))

    for plaintext in [ 'SOS', 'PYTHON', '12345' ]:
        testcase(plaintext)
