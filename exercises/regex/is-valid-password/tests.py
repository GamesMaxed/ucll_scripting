from testing import *
from testing.tests import *
from testing.assertions import *



with cumulative():
    with tested_function_name("is_valid_password"):
        invalid_passwords = [ 'a', 'aaaaaaaa', '7aTkffff', '7a!kqfpoifpo', 'a!kJFLoifpo' ]    
        valid_passwords = [ '7aT!ffff', '7 aA!         ', 'aBc123!!' ]

        for invalid_password in invalid_passwords:
            @test('is_valid_password({}) should return falsey value', repr(invalid_password))
            def _():
                must_be_falsey(tested_function(invalid_password))

        for valid_password in valid_passwords:
            @test('is_valid_password({}) must return truthy value', repr(valid_password))
            def _():
                must_be_truthy(tested_function(valid_password))

        for password in [ 'jf7!fjifjid',        \
                          'jfF!fjifjidd',       \
                          '78465163546546',     \
                          '$#$!*((*$(',         \
                          '                  ', \
                          'ffjlHJLKHffwq',      \
                          '16!ffJKLJdd ',       \
                          'ab7!D' ]:
            reftest(result=must_be_same_truthiness)(password)
