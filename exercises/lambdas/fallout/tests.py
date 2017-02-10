from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *


with cumulative(skip_after_fail=True):
    with tested_function_name('count_common_chars'), all_or_nothing():
        count_common_chars = reftest()

        count_common_chars('', '')
        count_common_chars('a', 'a')
        count_common_chars('a', 'b')
        count_common_chars('aa', 'aa')
        count_common_chars('ab', 'ba')
        count_common_chars('abcd', 'acbd')
        count_common_chars('', 'a')
        count_common_chars('123456', '123456')


    with tested_function_name('hack'), all_or_nothing():
        def create_evaluator(password, tries):
            tries_left = tries

            class SystemLockedError(Exception):
                pass
            
            def evaluator(attempt):
                nonlocal tries_left
                
                if tries_left == 0:
                    raise SystemLockedError()
                else:
                    tries_left -= 1
                    return reference_module().count_common_chars(attempt, password)

            return named_lambda('attempt'.format(tries, password), evaluator)

        def check(password, n, candidates):
            @test('Hacking password "{}", {} tries with candidates {}', password, n, candidates)
            def _():
                expected = reference_function(list(candidates), create_evaluator(password, n))
                actual = tested_function(list(candidates), create_evaluator(password, n))

                must_be_equal(expected, actual)


        check( 'abcd', 1, [ 'abcd' ] )
        check( 'axyd', 3, [ 'abcd', 'axyd', '1234', 'fdgh', 'dqdd' ] )
        check( 'abcd', 1, [ '1234', 'abcd' ] )

        candidates = [ 'abcd', 'abcx', 'xbcd', 'xbcy', 'axcy', 'a12d', 'a123', '1b23' ]
        for password in candidates:
            check( password, 3, candidates )
