import solution
import student
from testing import *


class PrimeTests(TestBuilder):
    def __init__(self):
        super().__init__(student)

    def tests(self):
        with self.group(cumulative()):
            def decodesTo(code, text):
                with self.group(context('{} should decode to {}', code, text)):
                    self.testFunction(lambda ensure: ensure.equals(text, student.decodeMorse(code)))

            decodesTo('', '')
            decodesTo('.-', 'A')
            decodesTo('... --- ...', 'SOS')
            decodesTo('.--. -.-- - .... --- -.', 'PYTHON')


def main():
    finalGrade = PrimeTests().runTests()
    print("Final grade: {0:.1f}/{1:2}".format(finalGrade.value, finalGrade.maximum))


main()
