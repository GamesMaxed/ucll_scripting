from testing import *
from testing.tests import *
from testing.assertions import *

with cumulative(), tested_function_name('demo'):
    @test('Demo test')
    def _():
        demo = reftest()

        for i in range(1, 11):
            demo(i)
