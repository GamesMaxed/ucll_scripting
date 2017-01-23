from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative:
    with testedFunctionName("isPrime"):
        def checkPrimality(n):
            if referenceFunction(n):
                @test("isPrime({}) should return truthy value", n)
                def check():
                    mustBeTruthy(testedFunction(n))
            else:
                @test("isPrime({}) should return falsey value", n)
                def check():
                    mustBeFalsey(testedFunction(n))

        for n in range(0, 100):
            checkPrimality(n)

    with testedFunctionName("nthPrime"):
        def checkNthPrime(n):
            expected = referenceFunction(n)
            
            @test("nthPrime({}) should return {}", n, expected)
            def check():
                mustBeEqual(expected, testedFunction(n))

        for n in range(1,50):
            checkNthPrime(n)

    with testedFunctionName("primesUpTo"):
        def listPrimes(n):
            expected = referenceFunction(n)
            
            @test("primesUpTo({}) should return {}", n, expected)
            def check():
                mustBeEqual(expected, testedFunction(n))

        for n in range(1, 50):
            listPrimes(n)
            
    with testedFunctionName("factorInteger"):
        def factor(n):
            expected = referenceFunction(n)
            
            @test("factorInteger({}) should return {}", n, expected)
            def check():
                mustBeEqual(expected, testedFunction(n))

        for n in range(1,50):
            factor(n)
