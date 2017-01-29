from testing import *
from testing.tests import *
from testing.assertions import *



with cumulative(), tested_function_name("find_repetition"):
    def repetition(string, repetition):
        @test('find_repetition({}) should return {}', repr(string), repr(repetition))
        def _():
            must_be_equal(repetition, tested_function(string))

    def no_repetition(string):
        @test('find_repetition({}) should return falsey value', repr(string))
        def _():
            must_be_falsey(tested_function(string))

    repetition('aaaabaaaa', 'aaaa')
    repetition('axxabaxxa', 'axxa')
    repetition('12341234', '1234')
    repetition('a1234bbbb1234c', '1234')
    no_repetition('aaaabaaa')
    no_repetition('123b123')
    no_repetition('aaaaaaa')

