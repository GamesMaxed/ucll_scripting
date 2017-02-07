from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("is_binary"), all_or_nothing():
        is_binary = reftest()

        is_binary('')
        is_binary('0')
        is_binary('1')
        is_binary('1010010')
        is_binary('2')
        is_binary('a')
        is_binary('10101015')
        is_binary('11010 10101')

    with tested_function_name("to_binary"), all_or_nothing():
        to_binary = reftest()

        for i in range(0,32):
            to_binary(i)

        @test("to_binary(-4) should throw exception")
        def _():
            must_raise( RuntimeError, lambda: tested_function(-4) )

    with tested_function_name("from_binary"), all_or_nothing():
        from_binary = reftest()

        for string in [ '0', '1', '10', '11', '101010', '111111', '000000' ]:
            from_binary(string)

        @test("from_binary('151') should throw exception")
        def _():
            must_raise( RuntimeError, lambda: tested_function('151') )
            
    with tested_function_name("has_extension"), all_or_nothing():
        has_extension = reftest()

        has_extension('foo.txt', 'txt')
        has_extension('bar.html', 'html')
        has_extension('baz.jpeg', 'jpeg')
        has_extension('qux.gz', 'gz')
        has_extension('footxt', 'txt')
        has_extension('bar.htm', 'html')
        has_extension('baz.jpeg2', 'jpeg')
        has_extension('a', 'zip')

    with tested_function_name('format_date'), all_or_nothing():
        format_date = reftest()

        format_date(1, 1, 2000)
        format_date(18, 12, 1980)
        format_date(25, 12, 1982)
        format_date(14, 12, 1986)

    with tested_function_name('format_time'), all_or_nothing():
        format_time = reftest()

        format_time(0, 0, 0, 0)
        format_time(10, 1, 2, 323)
        format_time(23, 59, 59, 999)
        format_time(12, 15, 0, 0)

    with tested_function_name('nth_digit'), all_or_nothing():
        nth_digit = reftest()

        nth_digit(123, 0)
        nth_digit(123, 1)
        nth_digit(123, 2)
        nth_digit(987654321, 0)
        nth_digit(987654321, 1)
        nth_digit(987654321, 2)
        nth_digit(987654321, 3)
        nth_digit(987654321, 4)
        nth_digit(987654321, 5)
        nth_digit(987654321, 6)
        nth_digit(-987654321, 0)
        nth_digit(-987654321, 1)
                
    with tested_function_name("balanced_parentheses"), all_or_nothing():
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
