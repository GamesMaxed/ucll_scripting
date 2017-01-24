from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative, testedFunctionName("containsTwice"):
    def yes(string, fragment):
        @test("containsTwice({}, {}) should return truthy value", repr(string), repr(fragment))
        def checkContainsTwice():
            mustBeTruthy(testedFunction(string, fragment))

    def no(string, fragment):
        @test("containsTwice({}, {}) should return falsey value", repr(string), repr(fragment))
        def checkNotContainsTwice():
            mustBeFalsey(testedFunction(string, fragment))
                    
    yes('aa', 'a')
    yes('axa', 'a')
    no('aaa', 'aa')
    yes('abcabc', 'abc')
    yes('abcxyzabc', 'abc')
    no('abcxyzab', 'abc')
    no('abxyzabc', 'abc')
    yes('ababab', 'ab')
    no('', 't')
    yes('', '')            

    for string, fragment in [ ('abcxabc', 'abc'), ('xyzabcxyz', 'xyz'), ('abxyzabc', 'abc'), ('', '') ]:
        reftest(result=mustBeSameTruthiness)(string, fragment)
