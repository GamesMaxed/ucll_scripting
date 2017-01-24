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

                printer = testing.environment.settings.printer

                printer.log(2, "SKIP: {} (in {})", self._name, testing.environment.tests.path)

                # Return 0/1
                return testing.score.Score(0, 1)
            else:
                try:
                    # Set test name
                    testing.environment.tests.push(testName = self._name)

                    # Run test
                    try:
                        self._function()
                    except TestFailure as e:
                        # If a regular test failure was raised, deal with it below
                        raise e
                    except Exception as e:
                        # If a different exception was raised, convert it to a TestFailure exception
                        if str(e):
                            contextString = "Exception {} raised: {}".format(type(e).__name__, str(e))
                        else:
                            contextString = "Exception {} raised".format(type(e).__name__)
                            
                        with context(contextString):
                            testing.assertions.fail()

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
    """
    Runs all child tests and adds their scores together.
    """
    def run(self):
        return sum( [ child.run() for child in self._children ], testing.score.Score(0, 0) )

class AllOrNothingTestSuite(_TestSuite):
    """
    Runs all child tests. If all child tests pass with a perfect
    score, returns 1/1. Otherwise, 0/1.
    """
    def run(self):
        if all([ child.run().isMaxScore() for child in self._children ]):
            return testing.score.Score(1, 1)
        else:
            return testing.score.Score(0, 1)

    
class _Scaler(_SingleChildTest):
    def __init__(self, maximum):
        super().__init__()
        self._maximum = maximum

    def run(self):
        return self._child.run().rescale(self._maximum)

cumulative = _TestContextManager(CumulativeTestSuite())

allOrNothing = _TestContextManager(AllOrNothingTestSuite())

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

def _getTestedFunction():
    """
    Fetches the test function.
    """
    return getattr(testing.environment.tests.testedModule, testing.environment.tests.testedFunctionName)

def _getReferenceFunction():
    """
    Fetches the test function.
    """
    return getattr(testing.environment.tests.referenceModule, testing.environment.tests.testedFunctionName)

def testedFunction(*args, **kwargs):
    """
    Calls the tested function with the provided arguments.
    """
    return _getTestedFunction()(*args, **kwargs)

def referenceFunction(*args, **kwargs):
    """
    Calls the reference function with the provided arguments.
    """
    return _getReferenceFunction()(*args, **kwargs)

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

def _limitStringLength(string, maxLength = 60):
    if len(string) > maxLength:
        return string[0:maxLength-3] + "..."
    else:
        return string

def reftest(result = None, arguments = None):
    compareResults = result or testing.assertions.mustBeEqual
    compareArguments = arguments or testing.assertions.ignore
    
    def testFunction(*args, **kwargs):
        argumentStrings = [ repr(arg) for arg in args ] + [ "{} = {}".format(key, repr(val)) for key, val in kwargs ]
        argumentString = "{}".format(", ".join(argumentStrings))

        # Call reference function
        refargs = copy.deepcopy(args)
        refkwargs = copy.deepcopy(kwargs)
        refretval = referenceFunction(*refargs, **refkwargs)

        name = "{}({}), refimpl returned {}".format(testedFunctionName(), argumentString, _limitStringLength(str(refretval)))
        
        @test(name)
        def referenceImplementationTest():
            with context('Comparing {}({}) with reference solution', testedFunctionName(), argumentString):
                # Call test implementation
                testargs = copy.deepcopy(args)
                testkwargs = copy.deepcopy(kwargs)
                testretval = testedFunction(*testargs, **testkwargs)

                # Compare return values
                with context("Comparing return values: expected {}, received {}", refretval, testretval):
                    compareResults(refretval, testretval)

                # Compare positional arguments
                for i in range(0, len(args)):
                    with context("Comparing positional argument #{}: expected {}, received {}", i, repr(refargs[i]), repr(testargs[i])):
                        compareArguments(refargs[i], testargs[i])

                # Compare keyword arguments
                for key in kwargs:
                    with context("Comparing keyword argument {}: expected {}, received {}", key, repr(refkwargs[key]), repr(testkwargs[i])):
                        compareArguments(refkwargs[key], testkwargs[i])

    return testFunction
