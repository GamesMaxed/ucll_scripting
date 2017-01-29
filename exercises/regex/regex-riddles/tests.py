from testing import *
from testing.tests import *
from testing.assertions import *
import dyn
from contextlib import contextmanager

with cumulative(skip_after_fail=True):
    env = dyn.create()

    @contextmanager
    def riddle(n):
        with env.let(riddle=n), all_or_nothing(), tested_function_name('riddle{}'.format(n)):
            yield
    
    def match(string):
        @test("Riddle {}: + {}", env.riddle, repr(string))
        def _():
            must_be_truthy( tested_function(string) )

    def no_match(string):
        @test("Riddle {}: - {}", env.riddle, repr(string))
        def _():
            must_be_falsey( tested_function(string) )

            
    with riddle(1):
        match('abc')
        match('xyz')
        match('123')
        match('fff')
        match('   ')

        no_match('')
        no_match('f')
        no_match('cc')
        no_match('1234')
        no_match('abcde')
        
    with riddle(2):
        match('')
        match('a')
        match('b')
        match('aaa')
        match('bbb')
        match('aabbbb')

        no_match('c')
        no_match('1')
        no_match('   ')
        no_match('ba')
        no_match('aba')

    with riddle(3):
        match('')
        match('a')
        match('b')
        match('aaa')
        match('bbb')
        match('aabbbb')
        match('ba')
        match('aba')
        match('ababababa')
        
        no_match('c')
        no_match('1')
        no_match('   ')
        no_match('abc')

    with riddle(4):
        match('aaaa')
        match('a a a a')
        match('abababa')
        match('   aaaa')
        match('aaaa    ')
        match('1a2a3a4a5')
        match('aaaaaaaaa')
        
        no_match('')
        no_match('a')
        no_match('aa')
        no_match('aaa')
        no_match('bbbb')
        no_match('1a2a3a4')
        
    with riddle(5):
        match('111')
        match('222')
        match('333')
        match('444')
        match('555')
        match('666')
        match('777')
        match('888')
        match('999')
        match('000')
        
        no_match('')
        no_match('1')
        no_match('11')
        no_match('123')
        no_match('abc')
        no_match(' 111')
        no_match('111 ')
        no_match('1111')
        
    with riddle(6):
        match('111')
        match('222')
        match('333')
        match('444')
        match('555')
        match('666')
        match('777')
        match('888')
        match('999')
        match('000')
        match('121212')
        match('123123123')
        match('767676')
        
        no_match('')
        no_match('1')
        no_match('11')
        no_match('123')
        no_match('abc')
        no_match(' 111')
        no_match('111 ')
        no_match('131415')
        no_match('12 12 12')

    with riddle(7):
        match('')
        match('a')
        match('fqljc')
        match(' f q c ldj')

        no_match('1')
        no_match('2')
        no_match('3')
        no_match('4')
        no_match('5')
        no_match('6')
        no_match('7')
        no_match('8')
        no_match('9')
        no_match('0')
        no_match('   3 ')
        no_match('djkl9jafjlk')

    with riddle(8):
        match('')
        match('a')
        match('b')
        match('c')
        match('ab')
        match('bc')
        match('ac')
        match('abc')

        no_match('x')
        no_match('4')
        no_match('aa')
        no_match('ba')
        no_match('cba')
        no_match(' a')
        no_match(' a')

    with riddle(9):
        match('aba')
        match('ktk')
        match('bob')
        match('121')
        match('ababa')
        match('58585')
        match('6d6d6d6')
        match('10101010101')
        match(' a a a a a ')

        no_match('')
        no_match('a')
        no_match('ab')
        no_match('abab')
        no_match('7575')
        no_match(' aba')
        no_match('aba ')

    with riddle(10):
        match('1')
        match('319')
        match('1+1')
        match('2-1')
        match('4*7')
        match('6/5')
        match('12+23')
        match('1+2+3+4+5')
        match('1*2*3*4*5')
        match('1-2-3-4-5')
        match('7/3/7/8/9')
        match('178+54-45*787+31/2')

        no_match('')
        no_match('x')
        no_match('7+')
        no_match(' 1')
        no_match('1 ')
        no_match('1 + 2')
        no_match('-8')
        no_match('7-5*')
        no_match('(1+2)*3')
