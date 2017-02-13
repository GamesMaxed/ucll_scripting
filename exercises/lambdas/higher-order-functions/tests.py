from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *


with cumulative():
    always_true = named_lambda('always_true', lambda x: True)
    always_false = named_lambda('always_false', lambda x: False)
    is_odd = named_lambda('is_odd', lambda x: x % 2 != 0)
    is_int = named_lambda('is_int', lambda x: type(x) == int)

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

    with tested_function_name('filter'), all_or_nothing():
        filter = reftest()

        filter([], always_true)
        filter([1], always_true)
        filter([1, 2], always_true)
        filter([1, 2, 3], always_true)
        filter([], always_false)
        filter([1], always_false)
        filter([1, 2], always_false)
        filter([1, 2, 3], always_false)
        filter([1, 2, 3, 4, 5], is_odd)
        filter([1, 'x', {4}, 9], is_int)

    with tested_function_name('all'), all_or_nothing():
        all = reftest()

        all([], always_true)
        all([1], always_true)
        all([1, 2], always_true)
        all([1, 2, 3], always_true)
        all([], always_false)
        all([1], always_false)
        all([1, 2], always_false)
        all([1, 2, 3], always_false)
        all([1, 2, 3, 4, 5], is_odd)
        all([1, 3, 5], is_odd)
        all([1, 'x', {4}, 9], is_int)
        all([1, 4, 9], is_int)

    with tested_function_name('any'), all_or_nothing():
        any = reftest()

        any([], always_true)
        any([1], always_true)
        any([1, 2], always_true)
        any([1, 2, 3], always_true)
        any([], always_false)
        any([1], always_false)
        any([1, 2], always_false)
        any([1, 2, 3], always_false)
        any([1, 2, 3, 4, 5], is_odd)
        any([1, 3, 5], is_odd)
        any([2, 4, 6], is_odd)
        any([1, 'x', {4}, 9], is_int)
        any(['x', {4}, '9'], is_int)
        any([1, 4, 9], is_int)
        
    with tested_function_name('memoize'), all_or_nothing():
        @test('memoize returns values of wrapped function')
        def _():
            def wrappee(x):
                return x

            wrapped = tested_function(wrappee)

            for x in range(1, 10):
                must_be_equal(wrappee(x), wrapped(x))
        
        @test('memoize calls function only once per input')
        def _():
            x = 0

            def wrappee(a):
                nonlocal x
                x += 1
                return x

            wrapped = tested_function(wrappee)

            must_be_equal(0, x)
            must_be_equal(1, wrapped(1))
            must_be_equal(1, x)
            must_be_equal(1, wrapped(1))
            must_be_equal(1, x)
            must_be_equal(2, wrapped(5))
            must_be_equal(2, x)
            must_be_equal(2, wrapped(5))
            must_be_equal(2, x)
            must_be_equal(1, wrapped(1))
            must_be_equal(3, wrapped(2))


    with tested_function_name('create_change_detector'), all_or_nothing():
        @test('create_change_detector does as advertized')
        def _():
            f = tested_function()

            must_be_truthy(f(0))
            must_be_falsey(f(0))
            must_be_truthy(f(1))
            must_be_falsey(f(1))
            must_be_truthy(f(0))
            must_be_truthy(f(1))
