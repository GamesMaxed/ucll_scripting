from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skip_after_fail=True):
    hash = reference_module().hash_password
    shash = reference_module().hash_salted_password
    
    with all_or_nothing(), tested_function_name('verify_password'):
        verify_password = reftest()

        verify_password('trapezoidal', hash('trapezoidal'))
        verify_password('password', hash('password'))
        verify_password('password', hash('xyz'))
        verify_password('', hash(''))

    with all_or_nothing(), tested_function_name('hash_salted_password'):
        hash_salted_password = reftest()

        hash_salted_password('dinosaur', '1234')
        hash_salted_password('pw', 'fakd45q')
        hash_salted_password('test', 'f')
        hash_salted_password('password', '787876')

    with all_or_nothing(), tested_function_name('verify_salted_password'):
        verify_salted_password = reftest()

        verify_salted_password('abcd', shash('abcd', '1234'), '1234')
        verify_salted_password('abcd', shash('abcde', '1234'), '1234')
        verify_salted_password('abcd', shash('abcd', '4321'), '1234')
        verify_salted_password('abcd', shash('abcdx', '4321'), '1234')
        
