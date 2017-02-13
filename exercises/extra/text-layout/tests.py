from testing import *
from testing.tests import *
from testing.assertions import *

with cumulative():
    with tested_function_name('split_lines_monospaced'), all_or_nothing():
        split_lines_monospaced = reftest()

        split_lines_monospaced('', 5)
        split_lines_monospaced('a', 5)
        split_lines_monospaced('ab cd', 5)
        split_lines_monospaced('ab cd', 2)
        split_lines_monospaced('abc de', 5)
        split_lines_monospaced('abc  de', 5)        
        split_lines_monospaced('123456789', 5)
        split_lines_monospaced('1 22 333 123456789 4444', 5)

        for i in range(3, 15):
            split_lines_monospaced("What's orange and sounds like a parrot?", i)
