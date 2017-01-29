from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(), tested_function_name("contains_twice"):
    def yes(string, fragment):
        @test("contains_twice({}, {}) should return truthy value", repr(string), repr(fragment))
        def _():
            must_be_truthy(tested_function(string, fragment))

    def no(string, fragment):
        @test("contains_twice({}, {}) should return falsey value", repr(string), repr(fragment))
        def _():
            must_be_falsey(tested_function(string, fragment))
                    
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
        reftest(result=must_be_same_truthiness)(string, fragment)
