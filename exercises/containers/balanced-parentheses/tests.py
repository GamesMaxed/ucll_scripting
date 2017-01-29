from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name("balanced_parentheses"):
    check = reftest()
    
    check('')
    check('(')
    check(')')
    check('())')
    check('(()')
    check('()()()()()')
    check('(((())))')
    check('((()((())())))')
    check('x(x)x')
    check('1(24)3((7)4)')
    check('1(24)3(7)4)')
