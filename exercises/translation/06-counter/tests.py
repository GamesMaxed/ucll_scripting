from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative:
    Counter = testedModule().Counter
    
    @test("Counter() initialized to 0")
    def counterInit():
        counter = Counter()
        mustBeEqual(0, counter.current())

    @test("Increment() increments counter")
    def counterIncrement():
        counter = Counter()
        counter.increment()
        mustBeEqual(1, counter.current())

    @test("Increment() increments counter")
    def counterReset():
        counter = Counter()
        counter.increment()
        counter.increment()
        counter.increment()
        counter.reset()
        mustBeEqual(0, counter.current())
        
