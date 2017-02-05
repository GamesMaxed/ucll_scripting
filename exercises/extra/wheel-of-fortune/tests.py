from testing import *
from testing.tests import *
from testing.assertions import *
from testing.conditions import *

import testing.conditions

with path('Puzzle'), cumulative(skip_after_fail=True), tested_class_name('Puzzle'):
    Puzzle = tested_class

    with path('initialization'), all_or_nothing():
        @test('cat is shown ___')
        def _():
            puzzle = Puzzle('Animal', 'cat')
            must_be_equal('___', puzzle.show())

        @test('sheep is shown _____')
        def _():
            puzzle = Puzzle('Animal', 'sheep')
            must_be_equal('_____', puzzle.show())

        @test('"a dog" is shown "_ ___"')
        def _():
            puzzle = Puzzle('Animal', 'a dog')
            must_be_equal('_ ___', puzzle.show())
