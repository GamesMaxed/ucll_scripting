from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skipAfterFail = False): ## TODO
    def Position(*args, **kwargs):
        return testedModule().Position(*args, **kwargs)

    def Sudoku(*args, **kwargs):
        return testedModule().Sudoku(*args, **kwargs)

    def RSudoku(*args, **kwargs):
        return referenceModule().Sudoku(*args, **kwargs)

    with path('Position'), cumulative():
        with path('__init__'):
            @test("initializes fields")
            def _():
                p = Position(5, 3)

                must_be_equal(5, p.x)
                must_be_equal(3, p.y)

        with path('equality'):
            @test("equal x and y => equal points")
            def _():
                p = Position(5, 3)
                q = Position(5, 3)

                must_be_equal(p, q)

            @test("unequal x => unequal points")
            def _():
                p = Position(1, 4)
                q = Position(5, 4)

                must_not_be_equal(p, q)

            @test("unequal y => unequal points")
            def _():
                p = Position(5, 3)
                q = Position(5, 4)

                must_not_be_equal(p, q)

            @test("comparing with non-Position yields falsey value")
            def _():
                p = Position(5, 3)
                q = 'hello'

                must_not_be_equal(p, q)
                
    with path('Sudoku'):
        with path('__init__'):
            @test("sets all squares to {{1, 2, 3, 4, 5, 6, 7, 8, 9}}")
            def _():
                sudoku = Sudoku()

                for y in range(0, 9):
                    for x in range(0, 9):
                        p = Position(x, y)
                        must_be_equal( {1, 2, 3, 4, 5, 6, 7, 8, 9}, sudoku[p] )

        with path('__getitem__ and __setitem__'):
            @test('setting changes grid')
            def _():
                sudoku = Sudoku()
                sudoku[Position(0,0)] = 5
                must_be_equal(5, sudoku[Position(0,0)])

        with path('allPositions'):
            @test('returns list of all positions')
            def _():
                sudoku = Sudoku()
                ref = RSudoku()
                
                mustContainSameElements( ref.allPositions(), sudoku.allPositions(), sameOrder=False )
