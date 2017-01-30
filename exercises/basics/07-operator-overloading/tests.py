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
        add(Fraction(-4, 5), Fraction(-2, 5))
        add(Fraction(1, 2), Fraction(2, 3))

    with path('__neg__'), all_or_nothing():
        def neg(a):
            ra = ref(a)
            
            @test('Negation of {} == {}', ra, -ra)
            def _test():
                expected = -ra
                actual = -a

                checkref(expected, actual)

        neg( Fraction(1, 1) )
        neg( Fraction(-2, 3) )
        neg( Fraction(0, 1) )
        neg( Fraction(-5, 2) )

    with path('__sub__'), all_or_nothing():
        def sub(a, b):
            ra = ref(a)
            rb = ref(b)
            
            @test('{} - {} == {}', ra, rb, ra - rb)
            def _test():
                expected = ra - rb
                actual = a - b

                checkref(expected, actual)

        sub( Fraction(1, 2), Fraction(1, 2) )
        sub( Fraction(2, 3), Fraction(-1, 3) )
        sub( Fraction(1, 1), Fraction(1, 5) )
        sub( Fraction(-3, 5), Fraction(1, 7) )
