from testing import *
from testing.tests import *
from testing.assertions import *


with path('Fraction'), cumulative(skip_after_fail=True):
    def Fraction(*args):
        return tested_module().Fraction(*args)

    def RFraction(*args):
        return reference_module().Fraction(*args)

    def check(fraction, numerator, denominator):
        with context('numerator'):
            must_be_equal(numerator, fraction.numerator)

        with context('denominator'):
            must_be_equal(denominator, fraction.denominator)

    def checkref(ref, actual):
        check(actual, ref.numerator, ref.denominator)

    def ref(fraction):
        return RFraction(fraction.numerator, fraction.denominator)
        

    with path('__init__'), all_or_nothing():
        @test('initializes fields')
        def _():
            a = Fraction(1, 2)
            check(a, 1, 2)

        @test('simplifies fraction')
        def _():
            a = Fraction(2, 4)
            check(a, 1, 2)

        @test('denominator is positive')
        def _():
            a = Fraction(7, -8)
            check(a, -7, 8)

        @test('zero fraction')
        def _():
            a = Fraction(0, 3)
            check(a, 0, 1)
            

    with path('__add__'), all_or_nothing():
        def add(a, b):
            ra = ref(a)
            rb = ref(b)
            
            @test('{} + {} == {}', ra, rb, ra + rb)
            def _test():
                expected = ra + rb
                actual = a + b

                checkref(expected, actual)

        add(Fraction(1, 5), Fraction(2, 5))
        add(Fraction(1, 2), Fraction(1, 2))
        add(Fraction(1, 2), Fraction(-1, 2))
