from testing import *
from testing.tests import *
from testing.assertions import *


with path('Counter'), cumulative():
    Counter = testedModule().Counter

    with path('__init__'):
        @test("initializes to 0")
        def _():
            counter = Counter()
            mustBeEqual(0, counter.current())

    with path('increment'):
        @test("increments counter")
        def _():
            counter = Counter()
            counter.increment()
            mustBeEqual(1, counter.current())

    with path('reset'):
        @test("sets value to 0")
        def _():
            counter = Counter()
            counter.increment()
            counter.increment()
            counter.increment()
            counter.reset()
            mustBeEqual(0, counter.current())
        
