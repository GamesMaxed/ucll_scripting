from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative():
    Person = testedModule().Person
    
    @test("[Person] Constructor initializes fields")
    def initializePerson():
        p = Person(80, 1.8)

        mustBeEqual(80, p.weight)
        mustBeEqual(1.8, p.height)

    @test("[Person] Setting weight")
    def setWeight():
        p = Person(45, 1.52)
        p.weight = 50

        mustBeEqual(50, p.weight)

    @test("[Person] Setting height")
    def setWeight():
        p = Person(45, 1.52)
        p.height = 1.50

        mustBeEqual(1.50, p.height)
        
    @test("[Person] Setting invalid weight should raise RuntimeError")
    def setInvalidWeight():
        p = Person(80, 1.8)

        def code():
            p.weight = -5
        
        mustRaise(RuntimeError, code)

    @test("[Person] Setting invalid height should raise RuntimeError")
    def setInvalidWeight():
        p = Person(80, 1.8)

        def code():
            p.height = -1

        mustRaise(RuntimeError, code)
    
    @test("[Person] Computing bmi")
    def bmi():
        p = Person(80, 1.8)

        mustBeEqual(80 / 1.8**2, p.bmi, epsilon = 0.0001)
