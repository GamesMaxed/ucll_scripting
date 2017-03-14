from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skip_after_fail=True):
    with all_or_nothing(), tested_function_name('next_generation'):
        next_generation = reftest()

        next_generation('0')
        next_generation('1')
    
        next_generation('000')
        next_generation('001')
        next_generation('010')
        next_generation('011')
        next_generation('100')
        next_generation('101')
        next_generation('110')
        next_generation('111')

        next_generation('100101101110110100010110101011')
        next_generation('001010101110100100100101000010')

    with all_or_nothing(), tested_function_name('compute_n_generations'):
        compute_n_generations = reftest()

        compute_n_generations( '0110101110001100', 2 )
        compute_n_generations( '01101', 10 )

