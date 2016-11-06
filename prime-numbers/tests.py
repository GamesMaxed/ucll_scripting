import solution
import student
from testing import *


class PrimeTests(TestBuilder):
    def __init__(self):
        super().__init__(student)

    def tests(self):
        with self.group(cumulative()):
            with self.group(context("isPrime"), scale(1), cumulative()):
                def mustBePrime(n):
                    with self.group(context('{} should be considered prime', n)):
                        self.testFunction(lambda ensure: ensure.true(student.isPrime(n)))
                    
                def mustNotBePrime(n):
                    with self.group(context('{} should not be considered prime', n)):
                        self.testFunction(lambda ensure: ensure.false(student.isPrime(n)))
            
                mustNotBePrime(0)
                mustNotBePrime(1)
                mustBePrime(4)

            with self.group(context("nthPrime"), cumulative()):
                def check(n, expected):
                    with self.group(context('Computing prime #{}', n)):
                        self.testFunction(lambda ensure: ensure.equals(expected, student.nthPrime(n)))

                check(1, 2)
                check(2, 3)
                check(3, 5)



def main():
    finalGrade = PrimeTests().runTests()
    print("Final grade: {0:.1f}/{1:2}".format(finalGrade.value, finalGrade.maximum))


main()
