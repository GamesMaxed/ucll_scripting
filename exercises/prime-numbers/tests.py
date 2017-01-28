from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with testedFunctionName("isPrime"):
        def checkPrimality(n):
            if referenceFunction(n):
                @test("isPrime({}) should return truthy value", n)
                def _():
                    mustBeTruthy(testedFunction(n))
            else:
                @test("isPrime({}) should return falsey value", n)
                def _():
                    mustBeFalsey(testedFunction(n))

        with allOrNothing():
            for n in range(0, 100):
                checkPrimality(n)

    with testedFunctionName("nthPrime"):
        def checkNthPrime(n):
            expected = referenceFunction(n)
            
            @test("nthPrime({}) should return {}", n, expected)
            def _():
                must_be_equal(expected, testedFunction(n))

        with allOrNothing():
            for n in range(1,50):
                checkNthPrime(n)

    with testedFunctionName("primesUpTo"):
        def listPrimes(n):
            expected = referenceFunction(n)
            
            @test("primesUpTo({}) should return {}", n, expected)
            def _():
                must_be_equal(expected, testedFunction(n))

        with allOrNothing():
            for n in range(1, 50):
                listPrimes(n)
            
    with testedFunctionName("factorInteger"):
        def factor(n):
            expected = referenceFunction(n)
            
            @test("factorInteger({}) should return {}", n, expected)
            def _():
                must_be_equal(expected, testedFunction(n))

        with allOrNothing():
            for n in range(1,50):
                factor(n)
