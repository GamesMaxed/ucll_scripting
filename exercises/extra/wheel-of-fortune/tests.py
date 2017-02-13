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

    with path('guess'), all_or_nothing():
        @test('Guessing t in "cat"')
        def _():
            puzzle = Puzzle('Animal', 'cat')
            count = puzzle.guess('t')

            must_be_equal(1, count)
            must_be_equal('__T', puzzle.show())

        @test('Guessing e in "elephant"')
        def _():
            puzzle = Puzzle('Animal', 'elephant')
            count = puzzle.guess('e')

            must_be_equal(2, count)
            must_be_equal('E_E_____', puzzle.show())
            
