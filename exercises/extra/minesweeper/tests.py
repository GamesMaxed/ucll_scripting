from testing import *
from testing.tests import *
from testing.assertions import *
from testing.conditions import *

import testing.conditions


with cumulative():
    def multiline_strip(string):
        return "\n".join( line.strip() for line in string.split("\n") if len(line.strip()) > 0 )

    def parse(string):
        def parse_char(ch):
            if ch.isdigit():
                return int(ch)
            else:
                return ch
            
        return [ [ parse_char(char) for char in line ] for line in string.split('\n') ]

    with tested_function_name('add_bombcounts'), all_or_nothing():
        bombcounts_ref = reftest(arguments=must_be_equal)

        def bombcounts(string):
            grid = parse(multiline_strip(string))
            bombcounts_ref(grid)

        def check(input, output):
            @test('Adding bombs to {}', input)
            def _():
                i = parse(multiline_strip(input))
                o = parse(multiline_strip(output))
                tested_function(i)
                
                must_be_equal(o, i)

        check('.', '0')
        check('B', 'B')
        check('..', '00')
        check('...', '000')
        check('B..', 'B10')
        check('B.B', 'B2B')
        check('B.B.B', 'B2B2B')
        check("""
              ...
              ...
              ...
              ""","""
              000
              000
              000
              """)
        check("""
              ...
              ...
              ...
              ""","""
              000
              000
              000
              """)
        check("""
              B..
              ...
              ...
              ""","""
              B10
              110
              000
              """)
        check("""
              .B.
              ...
              ...
              ""","""
              1B1
              111
              000
              """)
        check("""
              B.B
              ...
              B.B
              ""","""
              B2B
              242
              B2B
              """)
        
        bombcounts("""
                   ..........
                   ..........
                   ..........
                   ..........
                   ..........
                   """)
        bombcounts("""
                   B.......B.
                   .B.....B..
                   ..B...B...
                   ...B.B....
                   ....B.....
                   """)
        bombcounts("""
                   BBBBBBBBB.
                   .B..B..B..
                   ..B.B.B...
                   ...BBB....
                   ....B.....
                   """)
        bombcounts("""
                   .B.B......
                   B.B.B.....
                   .B.B...BBB
                   ..B....B.B
                   .......BBB
                   """)        
