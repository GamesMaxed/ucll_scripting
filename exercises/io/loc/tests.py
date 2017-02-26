from testing import *
from testing.tests import *
from testing.assertions import *
import os

with cumulative(skip_after_fail=True):
    with all_or_nothing(), tested_function_name('is_loc'):
        def is_loc(line):
            @test('is_loc({}) should return a truthy value', repr(line))
            def _():
                must_be_truthy(tested_function(line))

        def is_not_loc(line):
            @test('is_loc({}) should return a falsey value', repr(line))
            def _():
                must_be_falsey(tested_function(line))
                
        is_loc('def foo()')
        is_loc('    def foo()')
        is_loc('class Bar:')
        is_loc('    return 5 # five')

        is_not_loc('')
        is_not_loc('       ')
        is_not_loc('# test')
        is_not_loc('     # comment')

    with all_or_nothing(), tested_function_name('loc_in_file'):
        loc_in_file = reftest()

        loc_in_file('testdata/dyn.py')
        loc_in_file('testdata/testing/assertions.py')
        loc_in_file('testdata/testing/conditions.py')
        loc_in_file('testdata/testing/logging.py')

    with all_or_nothing(), tested_function_name('loc_in_directory'):
        loc_in_directory = reftest()

        loc_in_directory("testdata")
        loc_in_directory("testdata/testing")

