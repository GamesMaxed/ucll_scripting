from testing import *
from testing.tests import *
from testing.assertions import *


with path('Counter'), cumulative():
    Counter = tested_module().Counter

    with path('__init__'):
        @test("initializes to 0")
        def _():
            counter = Counter()
            must_be_equal(0, counter.current())

    with path('increment'):
        @test("increments counter")
        def _():
            counter = Counter()
            counter.increment()
            must_be_equal(1, counter.current())

    with path('reset'):
        @test("sets value to 0")
        def _():
            counter = Counter()
            counter.increment()
            counter.increment()
            counter.increment()
            counter.reset()
            must_be_equal(0, counter.current())
        
