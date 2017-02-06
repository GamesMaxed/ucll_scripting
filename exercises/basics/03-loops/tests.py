from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skip_after_fail=True):
    with tested_function_name("is_prime"), all_or_nothing():
        is_prime = reftest()

        for i in range(0,100):
            is_prime(i)

    with tested_function_name("count_primes_below"), all_or_nothing():
        count_primes_below = reftest()

        for i in range(0,100):
            count_primes_below(i)

    with tested_function_name("gcd"), all_or_nothing():
        gcd = reftest()

        quicktest(0, 0, 0)
        quicktest(5, 0, 5)
        quicktest(5, 20, 5)
        quicktest(13, 13 * 5, 13 * 7)
        quicktest(7, -7 * 5, -7 * 4)
        quicktest(7, -7 * 5, 7 * 4)
        quicktest(7, 7 * 5, -7 * 4)

        for i in [-1500, -80, -17, 0, 16, 41, 5000]:
            for j in [-2000, -10, -3, 0, 16, 59, 4000]:
                gcd(i, j)

    with tested_function_name("fibonacci"), all_or_nothing():
        fibonacci = reftest()

        for i in range(0, 20):
            fibonacci(i)
        
    with tested_function_name("sum_digits"), all_or_nothing():
        sum_digits = reftest()

        sum_digits(0)
        sum_digits(1)
        sum_digits(2)
        sum_digits(10)
        sum_digits(11)
        sum_digits(123)
        sum_digits(797546)
        sum_digits(-55)

    with tested_function_name("reverse_digits"), all_or_nothing():
        reverse_digits = reftest()

        reverse_digits(0)
        reverse_digits(1)
        reverse_digits(12)
        reverse_digits(123)
        reverse_digits(10)
        reverse_digits(-1)
        reverse_digits(-12)
        reverse_digits(123456789)
        
