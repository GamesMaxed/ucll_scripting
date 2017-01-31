from testing import *
from testing.tests import *
from testing.assertions import *
from testing.conditions import *

import testing.conditions

with path('Fraction'), cumulative(skip_after_fail=True), tested_class_name('Fraction'):
    Fraction = tested_class
    RFraction = reference_class

    def check(fraction, numerator, denominator):
        with context('numerator'):
            must_be_equal(numerator, fraction.numerator)

        with context('denominator'):
            must_be_equal(denominator, fraction.denominator)

    def checkref(ref, actual):
        check(actual, ref.numerator, ref.denominator)

    def frac(fraction):
        return Fraction(fraction.numerator, fraction.denominator)
        
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
        def add(ra, rb):
            @test('{} + {} == {}', ra, rb, ra + rb)
            def _test():
                a = frac(ra)
                b = frac(rb)

                expected = ra + rb
                actual = a + b

                checkref(expected, actual)

        add(RFraction(1, 5), RFraction(2, 5))
        add(RFraction(1, 2), RFraction(1, 2))
        add(RFraction(1, 2), RFraction(-1, 2))
        add(RFraction(-4, 5), RFraction(-2, 5))
        add(RFraction(1, 2), RFraction(2, 3))

    with path('__neg__'), all_or_nothing():
        def neg(ra):
            @test('Negation of {} == {}', ra, -ra)
            def _test():
                a = frac(ra)

                expected = -ra
                actual = -a

                checkref(expected, actual)

        neg( RFraction(1, 1) )
        neg( RFraction(-2, 3) )
        neg( RFraction(0, 1) )
        neg( RFraction(-5, 2) )

    with path('__sub__'), all_or_nothing():
        def sub(ra, rb):
            @test('{} - {} == {}', ra, rb, ra - rb)
            def _test():
                a = frac(ra)
                b = frac(rb)
                
                expected = ra - rb
                actual = a - b

                checkref(expected, actual)

        sub( RFraction(1, 2), RFraction(1, 2) )
        sub( RFraction(2, 3), RFraction(-1, 3) )
        sub( RFraction(1, 1), RFraction(1, 5) )
        sub( RFraction(-3, 5), RFraction(1, 7) )

    with path('__mul__'), all_or_nothing():
        def mul(ra, rb):
            @test('{} * {} == {}', ra, rb, ra * rb)
            def _test():
                a = frac(ra)
                b = frac(rb)
                
                expected = ra * rb
                actual = a * b

                checkref(expected, actual)

        mul( RFraction(0, 1), RFraction(5, 3) )
        mul( RFraction(1, 7), RFraction(0, 1) )
        mul( RFraction(1, 2), RFraction(1, 2) )
        mul( RFraction(1, 2), RFraction(2, 3) )
        mul( RFraction(5, 2), RFraction(7, 3) )
        mul( RFraction(-7, 2), RFraction(2, 7) )

    with path('invert'), all_or_nothing():
        def invert(ra):
            @test('Inversion of {} == {}', ra, ra.invert())
            def _test():
                a = frac(ra)

                expected = ra.invert()
                actual = a.invert()

                checkref(expected, actual)

        invert( RFraction(1, 1) )
        invert( RFraction(-2, 3) )
        invert( RFraction(4, 1) )
        invert( RFraction(-5, 2) )

    with path('__div__'), all_or_nothing():
        def div(ra, rb):
            @test('{} / {} == {}', ra, rb, ra / rb)
            def _test():
                a = frac(ra)
                b = frac(rb)
                
                expected = ra / rb
                actual = a / b

                checkref(expected, actual)

        div( RFraction(1, 2), RFraction(1, 2) )
        div( RFraction(5, 3), RFraction(7, 4) )
        div( RFraction(-1, 2), RFraction(4, 7) )
        div( RFraction(4, 3), RFraction(-7, 8) )
