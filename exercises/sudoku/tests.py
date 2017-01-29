from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skipAfterFail = False): ## TODO
    def _position(*args, **kwargs):
        return tested_module()._position(*args, **kwargs)

    def _sudoku(*args, **kwargs):
        return tested_module()._sudoku(*args, **kwargs)

    def R_sudoku(*args, **kwargs):
        return reference_module()._sudoku(*args, **kwargs)

    with path('_position'), cumulative():
        with path('__init__'):
            @test("initializes fields")
            def _():
                p = _position(5, 3)

                must_be_equal(5, p.x)
                must_be_equal(3, p.y)

        with path('equality'):
            @test("equal x and y => equal points")
            def _():
                p = _position(5, 3)
                q = _position(5, 3)

                must_be_equal(p, q)

            @test("unequal x => unequal points")
            def _():
                p = _position(1, 4)
                q = _position(5, 4)

                must_not_be_equal(p, q)

            @test("unequal y => unequal points")
            def _():
                p = _position(5, 3)
                q = _position(5, 4)

                must_not_be_equal(p, q)

            @test("comparing with non-_position yields falsey value")
            def _():
                p = _position(5, 3)
                q = 'hello'

                must_not_be_equal(p, q)
                
    with path('_sudoku'):
        with path('__init__'):
            @test("sets all squares to {{1, 2, 3, 4, 5, 6, 7, 8, 9}}")
            def _():
                sudoku = _sudoku()

                for y in range(0, 9):
                    for x in range(0, 9):
                        p = _position(x, y)
                        must_be_equal( {1, 2, 3, 4, 5, 6, 7, 8, 9}, sudoku[p] )

        with path('__getitem__ and __setitem__'):
            @test('setting changes grid')
            def _():
                sudoku = _sudoku()
                sudoku[_position(0,0)] = 5
                must_be_equal(5, sudoku[_position(0,0)])

        with path('all_positions'):
            @test('returns list of all positions')
            def _():
                sudoku = _sudoku()
                ref = R_sudoku()
                
                must_contain_same_elements( ref.all_positions(), sudoku.all_positions(), sameOrder=False )
