import solution
import student
from testing import *


with testedModule(student), referenceModule(solution), cumulative:
    with testedFunctionName("isValidPassword"):
        invalid_passwords = [ 'a', 'aaaaaaaa', '7aTkffff', '7a!kqfpoifpo', 'a!kJFLoifpo' ]    
        valid_passwords = [ '7aT!ffff', '7 aA!         ', 'aBc123!!' ]

        for invalid_password in invalid_passwords:
            @test("\"{}\" must be an invalid password", invalid_password)
            def checkInvalidPassword(invalid_password=invalid_password):
                isValidPassword = testedFunction()
                mustBeFalsey(isValidPassword(invalid_password))

        for valid_password in valid_passwords:
            @test("\"{}\" must be a valid password", valid_password)
            def checkValidPassword(valid_password=valid_password):
                isValidPassword = testedFunction()
                mustBeTruthy(isValidPassword(valid_password))


        for password in [ 'jf7!fjifjid',        \
                          'jfF!fjifjidd',       \
                          '78465163546546',     \
                          '$#$!*((*$(',         \
                          '                  ', \
                          'ffjlHJLKHffwq',      \
                          '16!ffJKLJdd ',       \
                          'ab7!D' ]:
            reftest('Verifying isValidPassword("{}")'.format(password), result=mustBeSameTruthiness)(password)


if __name__ == '__main__':
    runTests()
