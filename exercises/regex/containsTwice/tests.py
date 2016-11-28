import solution
import student
from testing import *


class PrimeTests(TestBuilder):
    def __init__(self):
        super().__init__(student)

    def tests(self):
        with self.group(cumulative()):
            def mustBeTrue(text, fragment):
                with self.group(context('{} contains {} twice', text, fragment)):
                    self.testFunction(lambda ensure: ensure.true(student.containsTwice(text, fragment)))

            def mustBeFalse(text, fragment):
                with self.group(context('{} does not contain {} twice', text, fragment)):
                    self.testFunction(lambda ensure: ensure.false(student.containsTwice(text, fragment)))

            mustBeTrue('aa', 'a')
            mustBeTrue('axa', 'a')
            mustBeFalse('aaa', 'aa')
            mustBeTrue('abcabc', 'abc')
            mustBeTrue('abcxyzabc', 'abc')
            mustBeFalse('abcxyzab', 'abc')
            mustBeFalse('abxyzabc', 'abc')
            mustBeTrue('ababab', 'ab')
            mustBeFalse('', 't')
            mustBeTrue('', '')            


def main():
    finalGrade = PrimeTests().runTests()
    print("Final grade: {0:.1f}/{1:2}".format(finalGrade.value, finalGrade.maximum))


main()
