from testing import *
from testing.tests import *
from testing.assertions import *
import os

with all_or_nothing(), tested_function_name('diff'):
    diff = reftest()

    files = [ "testdata/{}.txt".format(x) for x in "abc" ]

    for file1 in files:
        for file2 in files:
            diff(file1, file2)
