from testing import *
from testing.tests import *
from testing.assertions import *
import dyn
from contextlib import contextmanager

with cumulative():
    env = dyn.create()

    @contextmanager
    def riddle(n):
        with env.let(riddle=n), allOrNothing(), testedFunctionName('riddle{}'.format(n)):
            yield
    
    def match(string):
        @test("Riddle {}: + {}", env.riddle, repr(string))
        def check():
            mustBeTruthy( testedFunction(string) )

    def noMatch(string):
        @test("Riddle {}: - {}", env.riddle, repr(string))
        def check():
            mustBeFalsey( testedFunction(string) )

            
    with riddle(1):
        match('abc')
        match('xyz')
        match('123')
        match('fff')
        match('   ')

        noMatch('')
        noMatch('f')
        noMatch('cc')
        noMatch('1234')
        noMatch('abcde')
        
    with riddle(2):
        match('')
        match('a')
        match('b')
        match('aaa')
        match('bbb')
        match('aabbbb')

        noMatch('c')
        noMatch('1')
        noMatch('   ')
        noMatch('ba')
        noMatch('aba')

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
        
        noMatch('c')
        noMatch('1')
        noMatch('   ')
        noMatch('abc')

    with riddle(4):
        match('aaaa')
        match('a a a a')
        match('abababa')
        match('   aaaa')
        match('aaaa    ')
        match('1a2a3a4a5')
        match('aaaaaaaaa')
        
        noMatch('')
        noMatch('a')
        noMatch('aa')
        noMatch('aaa')
        noMatch('bbbb')
        noMatch('1a2a3a4')
        
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
        
        noMatch('')
        noMatch('1')
        noMatch('11')
        noMatch('123')
        noMatch('abc')
        noMatch(' 111')
        noMatch('111 ')
        noMatch('1111')
        
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
        
        noMatch('')
        noMatch('1')
        noMatch('11')
        noMatch('123')
        noMatch('abc')
        noMatch(' 111')
        noMatch('111 ')
        noMatch('131415')
        noMatch('12 12 12')

    with riddle(7):
        match('')
        match('a')
        match('fqljc')
        match(' f q c ldj')

        noMatch('1')
        noMatch('2')
        noMatch('3')
        noMatch('4')
        noMatch('5')
        noMatch('6')
        noMatch('7')
        noMatch('8')
        noMatch('9')
        noMatch('0')
        noMatch('   3 ')
        noMatch('djkl9jafjlk')

    with riddle(8):
        match('')
        match('a')
        match('b')
        match('c')
        match('ab')
        match('bc')
        match('ac')
        match('abc')

        noMatch('x')
        noMatch('4')
        noMatch('aa')
        noMatch('ba')
        noMatch('cba')
        noMatch(' a')
        noMatch(' a')

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

        noMatch('')
        noMatch('a')
        noMatch('ab')
        noMatch('abab')
        noMatch('7575')
        noMatch(' aba')
        noMatch('aba ')

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

        noMatch('')
        noMatch('x')
        noMatch('7+')
        noMatch(' 1')
        noMatch('1 ')
        noMatch('1 + 2')
        noMatch('-8')
        noMatch('7-5*')
        noMatch('(1+2)*3')
