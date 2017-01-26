from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skipAfterFail = True):
    def Position(*args, **kwargs):
        return testedModule().Position(*args, **kwargs)

    def Sudoku(*args, **kwargs):
        return testedModule().Sudoku(*args, **kwargs)

    with cumulative():
        with path("Position"):
            @test("Constructor initializes fields")
            def _():
                p = Position(5, 3)

                mustBeEqual(5, p.x)
                mustBeEqual(3, p.y)

            @test("Equal (x, y) => equal points")
            def _():
                p = Position(5, 3)
                q = Position(5, 3)

                mustBeEqual(p, q)

            @test("Unequal x => unequal points")
            def _():
                p = Position(1, 4)
                q = Position(5, 4)

                mustNotBeEqual(p, q)

            @test("Unequal y => unequal points")
            def _():
                p = Position(5, 3)
                q = Position(5, 4)

                mustNotBeEqual(p, q)

    with path("Sudoku"):
        @test("Initialization sets all squares to {{1, 2, 3, 4, 5, 6, 7, 8, 9}}")
        def _():
            sudoku = Sudoku()

            for y in range(0, 9):
                for x in range(0, 9):
                    p = Position(x, y)
                    mustBeEqual( {1, 2, 3, 4, 5, 6, 7, 8, 9}, sudoku[p] )

