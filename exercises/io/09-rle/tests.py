from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative(skip_after_fail=True):
    with all_or_nothing(), tested_function_name('compress'):
        compress = reftest()
        
        compress('')
        compress('a')
        compress('aa')
        compress('aaa')
        compress('aaaaaaa')
        compress('aaaaabbbbbbbbbaaaaaaa')
        compress('aabcccc ccddeeeee f g h')
        compress('AAAAaaaa')
        compress('(aa)(bbbbb)')

    with all_or_nothing(), tested_function_name('decompress'):
        decompress = reftest()
        
        decompress('')
        decompress('1a')
        decompress('2a')
        decompress('5a')
        decompress('5a3b8c')
        decompress('1a 1b 1c')
        decompress('7abc')
        decompress('(4b) (3c)')
        decompress('15a 10b')
