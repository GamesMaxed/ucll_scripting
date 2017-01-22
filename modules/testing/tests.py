from contextlib import contextmanager
import testing
import testing.conditions
import testing.score
import testing.assertions
import copy
import sys


class TestError(Exception):
    def __init__(self, message):
        super().__init__(message)

class TestFailure(TestError):
    def __init__(self):
        super().__init__("Failing assertion")

class InvalidTestCallError(TestError):
    def __init__(self):
        super().__init__("Calling test functions is disallowed")



class _TestContextManager:
    def __init__(self, *tests):
        super().__init__()
        self._tests = tests
        
    def __enter__(self):
        for test in self._tests:
            testing.environment.tests.top.addChild(test)
            testing.environment.tests.push(top=test)

    def __exit__(self, *args):
        for test in self._tests:
            testing.environment.tests.pop()



class _Test:
    """
    Superclass for all test classes.
    """
    pass

class _SingleChildTest(_Test):
    def __init__(self):
        super().__init__()
        self._child = None
        
    def addChild(self, child):
        if self._child != None:
            print("Only one child allowed in {}".format(type(self).__name__))
            print("Attempted to add {}".format(type(child).__name__))
            print("Existing child {}".format(type(self._child).__name__))
            sys.exit(-1)
        self._child = child

    def run(self):
        return self._child.run()

    def childCount(self):
        if self._child == None:
            return 0
        else:
            return 1
        

class RootTest(_SingleChildTest):
    pass


class _TestFunction(_Test):
    def __init__(self, name, function):
        self._name = name
        self._function = function
        self._testenvironment = testing.environment.tests.copy()

    def run(self):
        with testing.environment.let(tests = self._testenvironment):
            if not testing.environment.tests.condition():
                # Add current test to skip list
                testing.environment.run.skipped.append(self._name)

                # Return 0/1
                return testing.score.Score(0, 1)
            else:
                try:
                    # Set test name
                    testing.environment.tests.push(testName = self._name)

                    # Run test
                    self._function()

                    # Add test to pass list
                    testing.environment.run.passed.append(self._name)

                    # Return 1/1
                    return testing.score.Score(1, 1)

                except TestFailure:
                    # Add test to fail list
                    testing.environment.run.failed.append(self._name)

                    # Return 0/1
                    return testing.score.Score(0, 1)
            

class _TestSuite(_Test):
    def __init__(self):
        super().__init__()
        self._children = []

    def addChild(self, child):
        self._children.append(child)

    def childCount(self):
        return len(self._children)


class CumulativeTestSuite(_TestSuite):
    def run(self):
        return sum( [ child.run() for child in self._children ], testing.score.Score(0, 0) )

    
class _Scaler(_SingleChildTest):
    def __init__(self, maximum):
        super().__init__()
        self._maximum = maximum

    def run(self):
        return self._child.run().rescale(self._maximum)

cumulative = _TestContextManager(CumulativeTestSuite())

def scale(maximum):
    return _TestContextManager(_Scaler(maximum))

def testedModule(module = None):
    """
    If an argument is given, sets the dynamic variable testedModule
    to the given argument. If no argument is given, returns the
    current value of testedModule.
    """
    if module:
        return testing.environment.tests.let(testedModule = module)
    else:
        return testing.environment.tests.testedModule

def referenceModule(module = None):
    """
    If an argument is given, sets the dynamic variable referenceModule
    to the given argument. If no argument is given, returns the
    current value of referenceModule.
    """
    if module:
        return testing.environment.tests.let(referenceModule = module)
    else:
        return testing.environment.tests.referenceModule
    
def testedFunctionName(functionName = None):
    if functionName:
        @contextmanager
        def context():
            with testing.environment.tests.let(testedFunctionName = functionName), \
                 condition(testing.conditions.runIfFunctionExists(functionName)):
                yield

        return context()
    else:
        return testing.environment.tests.testedFunctionName

def testedFunction(*args, **kwargs):
    """
    Fetches the tested function.
    """
    return getattr(testing.environment.tests.testedModule, testing.environment.tests.testedFunctionName)(*args, **kwargs)

def referenceFunction(*args, **kwargs):
    """
    Fetches the reference function.
    """
    return getattr(testing.environment.tests.referenceModule, testing.environment.tests.testedFunctionName)(*args, **kwargs)

def context(message, *args, **kwargs):
    return testing.environment.tests.let(context = testing.environment.tests.context + [ message.format(*args, **kwargs) ])

def path(name, *args, **kwargs):
    return testing.environment.tests.let(path = testing.environment.tests.path + "/" + name.format(*args, **kwargs))

def condition(cond):
    """
    Adds an extra condition which needs to hold true
    for tests to be ran.
    """
    
    # Create conjunction of existing condition with new condition
    conjunction = testing.environment.tests.condition & cond

    # Update condition dynamic variable
    return testing.environment.tests.let(condition = conjunction)

def test(name, *args, **kwargs):
    """
    Decorator that turns the function into a test
    and adds it to the top test's children.
    """
    def wrapper(function):
        def _dummy():
            raise InvalidTestCallError()

        # Add test function as child to top test
        testing.environment.tests.top.addChild(_TestFunction(name.format(*args, **kwargs), function))
        return _dummy

    return wrapper
    
def reftest(name, result = None, arguments = None):
    compareResults = result or testing.assertions.mustBeEqual
    compareArguments = arguments or testing.assertions.ignore
    
    def testFunction(*args, **kwargs):
        @test(name)
        def referenceImplementationTest():
            argumentStrings = [ repr(arg) for arg in args ] + [ "{} = {}".format(key, repr(val)) for key, val in kwargs ]
            argumentString = "({})".format(", ".join(argumentStrings))
            
            with context('Comparing with reference implementation'), context('Called with arguments {}', argumentString):
                # Make copies of the arguments (they might be modified by the calls)
                testargs = copy.deepcopy(args)
                testkwargs = copy.deepcopy(kwargs)
                refargs = copy.deepcopy(args)
                refkwargs = copy.deepcopy(kwargs)

                # Call reference implementation
                refretval = referenceFunction(*refargs, **refkwargs)

                # Call test implementation
                testretval = testedFunction(*testargs, **testkwargs)

                # Compare return values
                with context("While comparing return values"):
                    compareResults(refretval, testretval)

                # Compare positional arguments
                for i in range(0, len(args)):
                    with context("While comparing positional argument #{}", i):
                        compareArguments(refargs[i], testargs[i])

                # Compare keyword arguments
                for key in kwargs:
                    with context("While comparing keyword argument {}", key):
                        compareArguments(refkwargs[key], testkwargs[i])

    return testFunction
