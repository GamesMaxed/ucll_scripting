from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    with tested_function_name("inverse_lookup"), all_or_nothing():
        inverse_lookup = reftest()

        inverse_lookup([])
        inverse_lookup([ 'a' ])
        inverse_lookup([ 'a', 'b' ])
        inverse_lookup([ 'a', 'b', 'c' ])
        inverse_lookup([ 'a', 'b', 'c', 'b' ])
        inverse_lookup([ 0, 1, 2, 3, 4 ])
        inverse_lookup([ 1, 1, 1, 1, 1 ])

    with tested_function_name('get_with_default'), all_or_nothing():
        get_with_default = reftest()

        get_with_default( {}, 'x', 0 )
        get_with_default( {}, 'x', 1 )
        get_with_default( {'x': 5}, 'x', 0 )
        get_with_default( {'x': 5, 'y': 7}, 'x', 0 )
        get_with_default( {'x': 5, 'y': 7}, 'y', 0 )
        get_with_default( {'x': 5, 'y': 7}, 'z', 0 )


    with tested_function_name('count_frequencies'), all_or_nothing():
        count_frequencies = reftest()

        count_frequencies( [] )
        count_frequencies( [ 'a' ] )
        count_frequencies( [ 'a', 'a' ] )
        count_frequencies( [ 'a', 'a', 'a' ] )
        count_frequencies( [ 'a', 'b' ] )
        count_frequencies( [ 'a', 'b', 'b' ] )
        count_frequencies( [ 'a', 'b', 'b', 'a' ] )


    with tested_function_name('css_lookup'), all_or_nothing():
        css_lookup = reftest()

        css_lookup( [], 'x', 0 )
        css_lookup( [], 'x', 4 )
        css_lookup( [ {'x': 3} ], 'x', 0 )
        css_lookup( [ {'x': 3}, {'x': 5} ], 'x', 0 )
        css_lookup( [ {'y': 3}, {'x': 5} ], 'x', 0 )
        css_lookup( [ {'y': 3}, {'x': 5} ], 'z', 0 )


    with tested_function_name('group_by_extension'), all_or_nothing():
        group_by_extension = reftest()

        group_by_extension( [] )
        group_by_extension( [ 'file.txt' ] )
        group_by_extension( [ 'foo.txt', 'bar.txt' ] )
        group_by_extension( [ 'foo.txt', 'bar.png' ] )
        group_by_extension( [ 'foo.txt', 'bar.txt', 'baz.png', 'qux.png' ] )


    with tested_function_name('word_width'), all_or_nothing():
        word_width = reftest()
        letter_widths = dict( zip("abcdefghijklmnopqrstuvwxyz", range(1,30)) )

        word_width(letter_widths, '')
        word_width(letter_widths, 'a')
        word_width(letter_widths, 'b')
        word_width(letter_widths, 'c')
        word_width(letter_widths, 'abc')
        word_width(letter_widths, 'abcdefghijklmnopqrstuvwxyz')
        word_width(letter_widths, 'abcdefghiklopqrtuxyz')
