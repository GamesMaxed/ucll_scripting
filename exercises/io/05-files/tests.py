from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name('files'):
    files = reftest()

    files('.')
    files('testdata')
    files('..')

