from testing import *
from testing.tests import *
from testing.assertions import *
import random


with cumulative(skip_after_fail = True):
    def Position(*args, **kwargs):
        return tested_module().Position(*args, **kwargs)

    def translate_position(p):
        return Position(p.x, p.y)

    def Sudoku(*args, **kwargs):
        return tested_module().Sudoku(*args, **kwargs)

    def RSudoku(*args, **kwargs):
        return reference_module().Sudoku(*args, **kwargs)

    with path('Position'), cumulative():
        with path('__init__'):
            @test("initializes fields")
            def _():
                p = Position(5, 3)

                must_be_equal(5, p.x)
                must_be_equal(3, p.y)

        with path('equality'), all_or_nothing():
            ref = RSudoku()

            for p in ref.all_positions():
                for q in ref.all_positions():
                    if p == q:
                        @test("{} and {} should be equal", p, q)
                        def _():
                            p2 = translate_position(p)
                            q2 = translate_position(q)

                            must_be_equal(p2, q2)
                    else:
                        @test("{} and {} should not be equal", p, q)
                        def _():
                            p2 = translate_position(p)
                            q2 = translate_position(q)

                            must_not_be_equal(p2, q2)

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

        with path('all_positions'):
            @test('returns list of all positions')
            def _():
                actual = Sudoku().all_positions()
                expected = [ Position(p.x, p.y) for p in RSudoku().all_positions() ]

                must_contain_same_elements(expected, actual, same_order=False)

        with path('copy'):
            @test('copy has same contents as original')
            def _():
                original = Sudoku()
                original[Position(4,1)] = 7
                copy = original.copy()

                for p in original.all_positions():
                    must_be_equal(original[p], copy[p])

            @test('copy can be changed without affecting original')
            def _():
                original = Sudoku()
                original[Position(6,5)] = 7
                copy = original.copy()
                copy[Position(6,5)] = 2

                must_be_equal(7, original[Position(6, 5)])

            @test("copy makes copies of the grid's elements")
            def _():
                original = Sudoku()
                original[Position(6,5)] = {1, 2, 3}
                copy = original.copy()
                copy[Position(6,5)].remove(1)

                must_be_equal({1, 2, 3}, original[Position(6, 5)])

        # with path('are_in_same_row'), all_or_nothing():
        #     ref = RSudoku()

        #     for p in ref.all_positions():
        #         for q in ref.all_positions():
        #             if ref.are_in_same_row(p, q):
        #                 @test('{} and {} should be in same row', p, q)
        #                 def _():
        #                     must_be_truthy(Sudoku().are_in_same_row(p, q))
        #             else:
        #                 @test('{} and {} should not be in same row', p, q)
        #                 def _():
        #                     must_be_falsey(Sudoku().are_in_same_row(p, q))
                            
        # with path('are_in_same_row'), all_or_nothing():
        #     ref = RSudoku()

        #     for p in ref.all_positions():
        #         for q in ref.all_positions():
        #             if ref.are_in_same_column(p, q):
        #                 @test('{} and {} should be in same column', p, q)
        #                 def _():
        #                     must_be_truthy(Sudoku().are_in_same_column(p, q))
        #             else:
        #                 @test('{} and {} should not be in same column', p, q)
        #                 def _():
        #                     must_be_falsey(Sudoku().are_in_same_column(p, q))
                            
        # with path('are_in_same_group'), all_or_nothing():
        #     ref = RSudoku()

        #     for p in ref.all_positions():
        #         for q in ref.all_positions():
        #             if ref.are_in_same_group(p, q):
        #                 @test('{} and {} should be in same group', p, q)
        #                 def _():
        #                     must_be_truthy(Sudoku().are_in_same_group(p, q))
        #             else:
        #                 @test('{} and {} should not be in same group', p, q)
        #                 def _():
        #                     must_be_falsey(Sudoku().are_in_same_group(p, q))
                            
        # with path('others_in_same_group'), all_or_nothing():
        #     ref = RSudoku()

        #     for p in ref.all_positions():
        #         @test('in same group as {}', p)
        #         def _():
        #             expected = [ translate_position(q) for q in ref.others_in_same_group(p) ]
        #             actual = Sudoku().others_in_same_group(translate_position(p))
                    
        #             must_contain_same_elements( expected, actual, same_order=False )

        with path('set'), all_or_nothing():
            @test('setting sets the grid contents at the given position')
            def _():
                sudoku = Sudoku()
                p = Position(3, 1)
                sudoku.set(p, 5)

                must_be_equal(5, sudoku[p])

            @test('setting removes the value from all other squares in the same group')
            def _():
                sudoku = Sudoku()
                p = Position(5, 8)
                n = 1
                sudoku.set(p, n)

                for q in sudoku.others_in_same_group(p):
                    must_be_falsey( n in sudoku[q] )

            @test('setting a previously set square to a different value raises Inconsistency')
            def _():
                sudoku = Sudoku()
                p = Position(3, 6)
                sudoku.set(p, 1)

                must_raise(tested_module().Inconsistency, lambda: sudoku.set(p, 2))

            @test('setting a square with a value already used in that row raises Inconsistency')
            def _():
                sudoku = Sudoku()
                sudoku.set(Position(1, 2), 1)

                must_raise(tested_module().Inconsistency, lambda: sudoku.set(Position(2, 2), 1))

            @test('setting a square with a value already used in that column raises Inconsistency')
            def _():
                sudoku = Sudoku()
                sudoku.set(Position(5, 4), 1)

                must_raise(tested_module().Inconsistency, lambda: sudoku.set(Position(5, 6), 1))

            @test('setting a square with a value already used in that block raises Inconsistency')
            def _():
                sudoku = Sudoku()
                sudoku.set(Position(0, 0), 9)

                must_raise(tested_module().Inconsistency, lambda: sudoku.set(Position(1, 1), 9))
                
            @test('cannot set a square that leads another square to have 0 options left')
            def _():
                sudoku = Sudoku()
                sudoku[Position(1,0)] = {1}

                must_raise(tested_module().Inconsistency, lambda: sudoku.set(Position(0,0), 1))

            @test('setting recursively sets all other certain squares')
            def _():
                sudoku = Sudoku()

                for x in range(0, 9):
                    sudoku[Position(x, 0)] = set(range(1, x+2))
                sudoku.set(Position(0,0), 1)

                for x in range(0, 9):
                    must_be_equal(sudoku[Position(x, 0)], x + 1)
                
