from testing import *
from testing.tests import *
from testing.assertions import *


with path('Person'), cumulative():
    Person = tested_module().Person

    with path('__init__'):
        @test("initializes fields")
        def _():
            p = Person(80, 1.8)

            must_be_equal(80, p.weight)
            must_be_equal(1.8, p.height)

    with path('weight'):
        @test("setting weight")
        def _():
            p = Person(45, 1.52)
            p.weight = 50

            must_be_equal(50, p.weight)

        @test("invalid weight should raise RuntimeError")
        def _():
            p = Person(80, 1.8)

            def code():
                p.weight = -5

            must_raise(RuntimeError, code)
            
    with path('height'):
        @test("setting height")
        def _():
            p = Person(45, 1.52)
            p.height = 1.50

            must_be_equal(1.50, p.height)
            
        @test("invalid height should raise RuntimeError")
        def _():
            p = Person(80, 1.8)

            def code():
                p.height = -1

            must_raise(RuntimeError, code)

    with path('bmi'):
        @test("yields correct result")
        def _():
            p = Person(80, 1.8)

            must_be_equal.with_epsilon(0.0001)(80 / 1.8**2, p.bmi)
