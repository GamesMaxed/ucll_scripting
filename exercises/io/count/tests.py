from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name('count_lines'):
    count_lines = reftest()

    count_lines('testdata/a.txt')
    count_lines('testdata/b.txt')
    count_lines('testdata/c.txt')
    
