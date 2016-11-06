import traceback
import copy

class TestError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FailureError(TestError):
    def __init__(self):
        super().__init__("Failing assertion")

class Score:
    def __init__(self, value, maximum):
        assert 0 <= value, "Score value must be positive"
        assert value <= maximum, "Score value ({}) must not be greater than maximum ({})".format(value, maximum)
        
        self.value = value
        self.maximum = maximum

    def __add__(self, other):
        return Score(self.value + other.value, self.maximum + other.maximum)

    def rescale(self, maximum):
        return Score(self.value / self.maximum * maximum, maximum)

    def __str__(self):
        return "{}/{}".format(self.value, self.maximum)


class Test:
    @classmethod
    def factory(cls, *args, **kwargs):
        return lambda parent: cls(parent, *args, *kwargs)

    def __init__(self, parent):
        self.parent = parent

    def context(self):
        if self.parent is not None:
            return self.parent.context()
        else:
            return []
        
    def __str__(self):
        return "\n".join(self.context())

    
class SingleChildTest(Test):
    def __init__(self, parent):
        super().__init__(parent)
        self.child = None

    def addChild(self, child):
        assert self.child is None, "SingleChildTest received multiple children"
        self.child = child
        
class TestSuite(Test):
    """
    Consists of subtests
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class CumulativeTestSuite(TestSuite):
    def __init__(self, parent):
        super().__init__(parent)

    def weight(self):
        return sum( [ child.weight() for child in self.children ] )
        
    def score(self):
        assert len(self.children) > 0, "CumulativeTestSuite must have at least one child"

        total = Score(0, 0)
        
        for child in self.children:
            score = child.score()
            total += score

        return total.rescale(1)

def cumulative():
    return CumulativeTestSuite.factory()


class ConditionalTest(SingleChildTest):
    """
    Single child test is run only if condition is true.
    """
    def __init__(self, parent, condition):
        super().__init__(parent)
        self.condition = condition

    def score(self):
        if self.condition:
            return self.child.score()
        else:
            return Score(0, self.child.weight())

class FunctionTest(Test):
    """
    Calls the given function. If no exceptions are thrown,
    returns score = 1, otherwise score = 0.
    """
    def __init__(self, parent, function):
        super().__init__(parent)
        self.function = function

    def score(self):
        try:
            self.function(Ensure(self.parent))
            return Score(1, 1)
        except TestError:
            return Score(0, 1)

class ContextDecorator(SingleChildTest):
    """
    Adds a context message.
    """
    def __init__(self, parent, context):
        super().__init__(parent)
        self.__context = context

    def score(self):
        return self.child.score()

    def context(self):
        return self.parent.context() + [ self.__context ]


def context(message, *args):
    return ContextDecorator.factory(message.format(*args))

    
class Scaler(SingleChildTest):
    """
    Scales the score
    """

    def __init__(self, parent, maximum):
        super().__init__(parent)
        self.__maximum = maximum

    def score(self):
        return self.child.score().rescale(self.__maximum)

    def weight(self):
        return self.__maximum


def scale(maximum):
    return Scaler.factory(maximum)
    

# class ReferenceImplementation(Test):
#     def __init__(self, parent):
#         super().__init__(parent)

#     def score(self):



# class ReferenceImplementation:
#     def __init__(self, context, reference, tested):
#         self.context = context
#         self.reference = reference
#         self.tested = tested
        
#     def addCase(self, *args, **kwargs):
#         @block
#         def test():
#             testArgs = copy.deepcopy(args)
#             testKwargs = copy.deepcopy(kwargs)
#             refArgs = copy.deepcopy(args)
#             refKwargs = copy.deepcopy(kwargs)
            
#             expected = self.reference(*refArgs, **refKwargs)
#             actual = self.tested(*testArgs, **testKwargs)

#             self.context.assertEquals(expected, actual)

#         test()
        
#     def __enter__(self):
#         return self
        
#     def __exit__(self, type, value, traceback):
#         pass


class TestBuilder:
    def __init__(self, module, root = Scaler(None, 20)):
        self.module = module
        self.__contextStack = [root]

    def __current(self):
        return self.__contextStack[-1]

    def __push(self, context):
        self.__contextStack.append(context)

    def __pop(self):
        self.__contextStack.pop()

    def child(self, function):
        self.__current().addChild(function)
        return function

    def __helper(self, factory):
        return TestBuilder.ContextStackHelper(self.__contextStack, factory)

    def __helpers(self, factories):
        return TestBuilder.HelperComposer( *[ self.__helper(factory) for factory in factories ] )

    def group(self, *factories):
        return self.__helpers(factories)        

    def testFunction(self, function = None):
        if function is None:
            # Used as decorator
            def wrapper(function):
                self.__current().addChild( FunctionTest(self.__current(), function) )
                return function
        
            return wrapper
        else:
            self.__current().addChild( FunctionTest(self.__current(), function) )

    def fromReferenceImplementation(self, referenceImplementation, testedImplementation, contextString = None):
        return TestBuilder.ReferenceImplementationHelper(self, self.__contextStack, referenceImplementation, testedImplementation, contextString=contextString)
        
    def runTests(self):
        self.tests()
        assert len(self.__contextStack) == 1, "Context stack bug"
        return self.__current().score()

    class ReferenceImplementationHelper:
        def __init__(self, parent, stack, referenceImplementation, testedImplementation, contextString):
            self.__parent = parent
            self.__stack = stack
            self.__refImpl = referenceImplementation
            self.__testedImpl = testedImplementation
            self.__contextString = contextString or "Called function with arguments ({inputs})"
                    

        def __call__(self, *args, **kwargs):
            expectedResult = self.__refImpl(*args, **kwargs)
            positionalArgsStrings = list(map(str, args))
            keywordArgsStrings = [ "{}={}".format(key, val) for key, val in kwargs ]
            contextMessage = self.__contextString.format(inputs=",".join(positionalArgsStrings + keywordArgsStrings))
            
            def tester(ensure):
                actualResult = self.__testedImpl(*args, **kwargs)
                ensure.equals(expectedResult, actualResult)

            with self.__parent.group(context(contextMessage)):
                self.__parent.testFunction(function = tester)

        def __enter__(self):
            self.__stack.append( cumulative()( self.__stack[-1] ) )

            return self

        def __exit__(self, type, value, traceback):
            top = self.__stack.pop()
            self.__stack[-1].addChild(top)
            

    class ContextStackHelper:
        def __init__(self, stack, factory):
            self.stack = stack
            self.factory = factory
    
        def __enter__(self):
            self.stack.append(self.factory(self.stack[-1]))
            
        def __exit__(self, type, value, traceback):
            top = self.stack.pop()
            self.stack[-1].addChild(top)

    class HelperComposer:
        def __init__(self, *components):
            self.__components = components

        def __enter__(self):
            for component in self.__components:
                component.__enter__()

        def __exit__(self, type, value, traceback):
            for component in reversed(self.__components):
                component.__exit__(type, value, traceback)

class Ensure:
    def __init__(self, parent):
        self.__parent = parent

    def fail(self, message, *args):
        print(self.__parent)
        print(message.format(*args))
        print('---')
        raise FailureError()

    def equals(self, expected, actual):
        if expected != actual:
            self.fail("Expected {}, received {}", expected, actual)

    def true(self, value):
        self.equals(True, value)

    def false(self, value):
        self.equals(False, value)

