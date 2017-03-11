from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name('contents'):
    contents = reftest()

    contents('tests.py')
    contents('solution.py')
