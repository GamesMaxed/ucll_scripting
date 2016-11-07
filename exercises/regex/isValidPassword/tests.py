import solution
import student
from testing import *


class PrimeTests(TestBuilder):
    def __init__(self):
        super().__init__(student)

    def tests(self):
        with self.group(cumulative()):
            def mustBeValid(password):
                with self.group(context('{} should be considered valid', password)):
                    self.testFunction(lambda ensure: ensure.true(student.isValidPassword(password)))

            def mustBeInvalid(password):
                with self.group(context('{} should be considered invalid', password)):
                    self.testFunction(lambda ensure: ensure.false(student.isValidPassword(password)))

            mustBeInvalid('a')
            mustBeInvalid('aaaaaaaa')
            mustBeValid('7aT!ffff')
            mustBeInvalid('7aTkffff')
            mustBeInvalid('7a!kqfpoifpo')
            mustBeInvalid('a!kJFLoifpo')
            mustBeValid('7 aA!         ')
            
            with self.fromReferenceImplementation(solution.isValidPassword, student.isValidPassword, contextString="isPrime({inputs})") as addCase:
                addCase('jf7!fjifjid')
                addCase('jfF!fjifjidd')
                addCase('78465163546546')
                addCase('$#$!*((*$(')
                addCase('                  ')
                addCase('ffjlHJLKHffwq')
                addCase('16!ffJKLJdd ')
                addCase('ab7!D')



def main():
    finalGrade = PrimeTests().runTests()
    print("Final grade: {0:.1f}/{1:2}".format(finalGrade.value, finalGrade.maximum))


main()
