from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing():
    with tested_function_name("tree"):
        tree = reftest()
        
        tree('.')
        tree('testdata')
        tree('..')
