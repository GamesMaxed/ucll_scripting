from testing import *
from testing.tests import *
from testing.assertions import *



with cumulative, testedFunctionName("findRepetition"):
    def repetition(string, repetition):
        @test('findRepetition({}) should return {}', repr(string), repr(repetition))
        def checkRepetition():
            mustBeEqual(repetition, testedFunction(string))

    def noRepetition(string):
        @test('findRepetition({}) should return falsey value', repr(string))
        def checkNoRepetition():
            mustBeFalsey(testedFunction(string))

    repetition('aaaabaaaa', 'aaaa')
    repetition('axxabaxxa', 'axxa')
    repetition('12341234', '1234')
    repetition('a1234bbbb1234c', '1234')
    noRepetition('aaaabaaa')
    noRepetition('123b123')
    noRepetition('aaaaaaa')

