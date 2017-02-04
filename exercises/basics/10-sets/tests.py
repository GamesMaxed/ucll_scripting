from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("create_interval"), all_or_nothing():
        create_interval = reftest()

        create_interval(0, 0)
        create_interval(0, 10)
        create_interval(4, 12)
        create_interval(9, 5)

