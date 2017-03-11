from testing import *
from testing.tests import *
from testing.assertions import *
import os

with cumulative(skip_after_fail=False):
    with all_or_nothing(), tested_function_name('is_loc'):
        def is_loc(line, delimiter):
            @test('is_loc({}, {}) should return a truthy value', repr(line), repr(delimiter))
            def _():
                must_be_truthy(tested_function(line, delimiter))

        def is_not_loc(line, delimiter):
            @test('is_loc({}, {}) should return a falsey value', repr(line), repr(delimiter))
            def _():
                must_be_falsey(tested_function(line, delimiter))

        for delimiter in [ '#', '//', '%', '--' ]:
            is_loc('def foo()', delimiter)
            is_loc('    def foo()', delimiter)
            is_loc('class Bar:', delimiter)
            is_loc('    return 5 {} five'.format(delimiter), delimiter)

            is_not_loc('', delimiter)
            is_not_loc('       ', delimiter)
            is_not_loc('{} test'.format(delimiter), delimiter)
            is_not_loc('     {} comment'.format(delimiter), delimiter)

            
    with all_or_nothing(), tested_function_name('extension_of'):
        extension_of = reftest()
        
        extension_of('a.py')
        extension_of('bb.rb')
        extension_of('ccc.cl')
        extension_of('dddd.tex')
        extension_of('eeeee.java')
        extension_of('ffffff.cpp')
        extension_of('sjdklj.hs')
        extension_of('fffffff.adsd.cpp')

    with all_or_nothing(), tested_function_name('is_source_file'):
        is_source_file = reftest()
        
        is_source_file('a.txt')
        is_source_file('x.py')
        is_source_file('bdf.rb')
        is_source_file('fdff.cpp')
        is_source_file('ffff.java')
        is_source_file('fdfda.tex')
        is_source_file('fdfdf.cl')
        is_source_file('fdfdfdq.hs')

    with all_or_nothing(), tested_function_name('comment_delimiter_for'):
        comment_delimiter_for = reftest()

        comment_delimiter_for('x.rb')
        comment_delimiter_for('fx.py')
        comment_delimiter_for('dfx.java')
        comment_delimiter_for('hgd.cpp')
        comment_delimiter_for('fsdq.tex')
        comment_delimiter_for('ggfq.cl')
        comment_delimiter_for('ghf.hs')

    with all_or_nothing(), tested_function_name('loc'):
        loc = reftest()

        loc('', '#')
        loc('x', '#')
        loc('xyz', '#')
        loc('  x', '#')
        loc('  xyz', '#')
        loc('   # x', '#')
        loc('   -- xfgf', '--')
        loc("""
        x
        y
        """, '//')
        loc("""
        x
        y
            // qq
            qdf // pp

        ff
        """, '//')

        
    with all_or_nothing(), tested_function_name('loc_in_file'):
        loc_in_file = reftest()

        loc_in_file('testdata/a.py')
        loc_in_file('testdata/b.rb')
        loc_in_file('testdata/c.cpp')
        loc_in_file('testdata/d.cl')

    with all_or_nothing(), tested_function_name('loc_in_directory'):
        loc_in_directory = reftest()

        loc_in_directory(".")
        loc_in_directory("..")
        loc_in_directory("testdata")

