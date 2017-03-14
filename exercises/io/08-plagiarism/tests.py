from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name('plagiarism'):
    plagiarism = reftest()

    plagiarism( ['testdata/a.txt'] )
    plagiarism( ['testdata/a.txt', 'testdata/b.txt'] )
    plagiarism( ['testdata/a.txt', 'testdata/b.txt', 'testdata/c.txt'] )
    plagiarism( ['testdata/a.txt', 'testdata/b.txt', 'testdata/c.txt', 'testdata/d.txt'] )
