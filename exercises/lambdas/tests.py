from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *


with cumulative():
    always_true = named_lambda('always_true', lambda x: True)
    always_false = named_lambda('always_false', lambda x: False)
    is_odd = named_lambda('is_odd', lambda x: x % 2 != 0)
    is_int = named_lambda('is_odd', lambda x: type(x) == int)

    get_type = named_lambda('get_type', lambda x: type(x).__name__)
    


    with tested_function_name('count'), all_or_nothing():
        count = reftest()

        count([], always_true)
        count([1], always_true)
        count([1, 2, 3], always_true)
        count([], always_false)
        count([1], always_false)
        count([1, 2, 3], always_false)
        count([1, 2, 3], is_odd)
        count([1, 2, 3, 4, 5], is_odd)
        count([1, 2, 3, 4, 5], is_int)
        count(['x', 1, '4', 2], is_int)

    with tested_function_name('find_first'), all_or_nothing():
        find_first = reftest()

        find_first([], always_true, 1)
        find_first([], always_true, None)
        find_first([], always_true, 'default')
        find_first([1], always_true, 1)
        find_first([1, 2], always_true, 1)
        find_first([1, 2, 3], always_true, 1)
        find_first([1], always_false, 7)
        find_first([1, 2], always_false, 4)
        find_first([1, 2, 3], always_false, 99)

    with tested_function_name('group_by_key'), all_or_nothing():
        group_by_key = reftest()

        group_by_key([], get_type)
        group_by_key([1], get_type)
        group_by_key([1, 2], get_type)
        group_by_key(['x'], get_type)
        group_by_key([1, 'x'], get_type)
        group_by_key([1, 'x', [1,2], {1,2}], get_type)
        group_by_key([1, 2, 3, 4, 5], is_odd)
