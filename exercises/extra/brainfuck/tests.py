from testing import *
from testing.tests import *
from testing.assertions import *
from testing.conditions import *

import testing.conditions

with path('VirtualMachine'), cumulative(skip_after_fail=True), tested_class_name('VirtualMachine'):
    VirtualMachine = tested_class

    def array_reader(xs):
        i = 0

        def reader():
            nonlocal i
            
            x = xs[i]
            i += 1
            return x

        return reader

    def array_writer():
        xs = []

        def writer(x):
            xs.append(x)

        return (xs, writer)


    def must_be_memory(vm, expected):
        for index, value in zip(range(0, len(expected)), expected):
            with context('Expecting memory location {} to be equal to {}', index, value):
                must_be_equal(expected[index], vm.memory(index))

    def check(code, memory = None, input = '', output = None):
        @test('Running "{}"', code, memory)
        def _():
            out, writer = array_writer()
            vm = VirtualMachine(code, array_reader(input), writer)
            vm.run()

            if memory:
                must_be_memory(vm, memory)

            if output:
                must_be_equal(output, out)
    
    check('', memory = [0] * 10)
    check('+', memory = [1])
    check('++', memory = [2])
    check('>+', memory = [0, 1])
    check('+>+', memory = [1, 1])
    check('+>+>+', memory = [1, 1, 1])
    check('+>+>+<-<-', memory = [0, 0, 1])
    check('[]', memory = [0] * 10)
    check('+[-]', memory = [0] * 10)
    check('++++[>+<-]', memory = [0, 4])
    check('++++[>++++[>+<-]<-]', memory = [0, 0, 16])
    check('.', output = [0])
    check('..', output = [0, 0])
    check('+..', output = [1, 1])
    check('+..+..', output = [1, 1, 2, 2])
    check('+++++[.-].', output = [5, 4, 3, 2, 1, 0])
    check(',.', input = [1], output = [1])
    check(',[>++<-]>.', input = [1], output = [2])
    check(',[>++<-]>.', input = [2], output = [4])
    check(',[>++<-]>.', input = [3], output = [6])
    check(',[>+++<-]>.', input = [3], output = [9])
    check(',[>+>+<<-]', input = [4], memory = [0,4,4])
    check(',>,[>+>+<<-]', input = [4, 3], memory = [4, 0, 3, 3])
    check(',>,<[>>+<<-]>[>+<-]>.', input = [0, 0], output = [0])


