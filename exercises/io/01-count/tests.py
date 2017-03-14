from testing import *
from testing.tests import *
from testing.assertions import *
import io


with cumulative(skip_after_fail=True):
    with all_or_nothing(), tested_function_name('count_lines'):
        count_lines_ref = reftest()

        def count_lines(string):
            with context('Line count of\n"""\n{}\n"""', string):
                count_lines_ref(io.StringIO(string))

        count_lines('')
        count_lines('x')
        count_lines('x\nx')
        count_lines('x\nx\nx')
        count_lines('xx')
        count_lines('xx\nxxxx')
        count_lines('x\n' * 5)
        count_lines('xx\n' * 7)
        count_lines('xxx\n' * 8)

    with all_or_nothing(), tested_function_name('count_words'):
        count_words_ref = reftest()

        def count_words(string):
            with context('Word count of\n"""\n{}\n"""', string):
                count_words_ref(io.StringIO(string))

        count_words('')
        count_words('x x')
        count_words('x x x')
        count_words('x x x x')
        count_words('x\nx')
        count_words('x xxxx')
        count_words('x\nx\tx x')
        count_words('a\ns fy xx')

    with all_or_nothing(), tested_function_name('count_chars'):
        count_chars_ref = reftest()

        def count_chars(string):
            with context('Char count of\n"""\n{}\n"""', string):
                count_chars_ref(io.StringIO(string))

        count_chars('')
        count_chars('x')
        count_chars('xx')
        count_chars('x x')
        count_chars('x x\nx x')
        count_chars('abcd\nefgh')
