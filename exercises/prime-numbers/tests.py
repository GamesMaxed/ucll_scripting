from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("is_prime"):
        def check_primality(n):
            if reference_function(n):
                @test("is_prime({}) should return truthy value", n)
                def _():
                    must_be_truthy(tested_function(n))
            else:
                @test("is_prime({}) should return falsey value", n)
                def _():
                    must_be_falsey(tested_function(n))

        with all_or_nothing():
            for n in range(0, 100):
                check_primality(n)

    with tested_function_name("nth_prime"):
        def check_nth_prime(n):
            expected = reference_function(n)
            
            @test("nth_prime({}) should return {}", n, expected)
            def _():
                must_be_equal(expected, tested_function(n))

        with all_or_nothing():
            for n in range(1,50):
                check_nth_prime(n)

    with tested_function_name("primes_up_to"):
        def list_primes(n):
            expected = reference_function(n)
            
            @test("primes_up_to({}) should return {}", n, expected)
            def _():
                must_be_equal(expected, tested_function(n))

        with all_or_nothing():
            for n in range(1, 50):
                list_primes(n)
            
    with tested_function_name("factor_integer"):
        def factor(n):
            expected = reference_function(n)
            
            @test("factor_integer({}) should return {}", n, expected)
            def _():
                must_be_equal(expected, tested_function(n))

        with all_or_nothing():
            for n in range(1,50):
                factor(n)
