from contextlib import contextmanager
import importlib
import argparse
import copy
import sys
import dyn
import os


def checkPythonVersion():
    version = sys.version_info

    if version.major < 3 or (version.major == 3 and version.minor < 5):
        sys.exit("You need at least Python 3.5")

checkPythonVersion()



#
# Test exception classes
#
class TestError(Exception):
    def __init__(self, message):
        super().__init__(message)

class TestFailure(TestError):
    def __init__(self):
        super().__init__("Failing assertion")

class InvalidTestCallError(TestError):
    def __init__(self):
        super().__init__("Calling test functions is disallowed")


#
# Score
#
class Score:
    """
    Represents a score.

    Scores are not to be confused with fractions.
    For example, a score of 5/10 is not the same as a score of 1/2.
    Score addition also follows different rules.
    """
    def __init__(self, value, maximum):
        assert 0 <= value, "Score value must be positive"
        assert value <= maximum, "Score value ({}) must not be greater than maximum ({})".format(value, maximum)
        
        self.value = value
        self.maximum = maximum

    def __add__(self, other):
        """
        Adds two scores together.

        a/b + c/d = (a+c)/(b+d).
        """
        return Score(self.value + other.value, self.maximum + other.maximum)

    def rescale(self, maximum):
        """
        Rescales the score to a given maximum.
        """
        return Score(self.value / self.maximum * maximum, maximum)

    def __str__(self):
        return "{}/{}".format(self.value, self.maximum)


class _TestPredicate:
    """
    Used to determine whether to run a test or not.
    """
    def __init__(self, name, predicate):
        self._name = name
        self._predicate = predicate
        
    def __call__(self):
        return self._predicate()

    def __and__(self, other):
        def check():
            return self() & other()
        return _TestPredicate( "{} & {}".format(str(self), str(other)), check )

    def __str__(self):
        return self._name


runAlways = _TestPredicate("always", lambda: True)
runNever = _TestPredicate("never", lambda: False)

def runIfFunctionExists(functionName):
    if not _environment.tests.isBound('testedModule'):
        raise TestError("No tested module set")
    else:
        def check():
            return functionName in dir(_environment.tests.testedModule)
        
        return _TestPredicate("run if {} exists".format(functionName), check)


def limitTestCount():
    def check():
        return len(_environment.run.passed) + len(_environment.run.failed) < _environment.settings.maxTests

    return _TestPredicate("limit test count", check)


#
# Test classes
#

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
        assert self._child == None, "Only one child allowed in {}, cannot add {}".format( type(self).__name__, type(child).__name__ )
        self._child = child

    def run(self):
        return self._child.run()
        

class _RootTest(_SingleChildTest):
    pass


class _TestFunction(_Test):
    def __init__(self, name, function):
        self._name = name
        self._function = function
        self._testenvironment = _environment.tests.copy()

    def run(self):
        with _environment.let(tests = self._testenvironment):
            if not _environment.tests.condition():
                # Add current test to skip list
                _environment.run.skipped.append(self._name)

                # Return 0/1
                return Score(0, 1)
            else:
                try:
                    # Set test name
                    _environment.tests.push(testName = self._name)

                    # Run test
                    self._function()

                    # Add test to pass list
                    _environment.run.passed.append(self._name)

                    # Return 1/1
                    return Score(1, 1)

                except TestFailure:
                    # Add test to fail list
                    _environment.run.failed.append(self._name)

                    # Return 0/1
                    return Score(0, 1)
            

class _TestSuite(_Test):
    def __init__(self):
        super().__init__()
        self._children = []

    def addChild(self, child):
        self._children.append(child)


class _CumulativeTestSuite(_TestSuite):
    def run(self):
        return sum( [ child.run() for child in self._children ], Score(0, 0) )

    
class _Scaler(_SingleChildTest):
    def __init__(self, maximum):
        super().__init__()
        self._maximum = maximum

    def run(self):
        return self._child.run().rescale(self._maximum)


#
# Printer
#

class _Printer:
    def log(self, verbosity, message, *args, **kwargs):
        if _environment.settings.verbosity >= verbosity:
            print(message.format(*args, **kwargs))
        



# Create root test
_rootTest = _RootTest()

_environment = dyn.create()
_environment.push(tests = dyn.create(), settings = dyn.create(), run = dyn.create())
_environment.tests.push(top=_rootTest, context=[], path="", condition = limitTestCount())


def _dummy():
    raise InvalidTestCallError()


class _TestContextManager:
    def __init__(self, *tests):
        super().__init__()
        self._tests = tests
        
    def __enter__(self):
        for test in self._tests:
            _environment.tests.top.addChild(test)
            _environment.tests.push(top=test)

    def __exit__(self, *args):
        for test in self._tests:
            _environment.tests.pop()


def findFirst(xs, predicate):
    for x in xs:
        if predicate(x):
            return x
            
def _firstExternalStackFrame():
    """
    Returns the first external stack frame, i.e. the
    first stack frame whose function does not reside
    in this file.
    """
    # Fetch call stack
    callStack = inspect.stack()

    print([(frame.filename, frame.lineno) for frame in callStack])

    # Look for first stack frame belonging to code
    # that does not reside in this file
    externalStackFrame = findFirst(callStack, lambda frame: frame.filename != __file__)

    return externalStackFrame
        

cumulative = _TestContextManager(_CumulativeTestSuite())

def scale(maximum):
    return _TestContextManager(_Scaler(maximum))

def testedModule(module = None):
    """
    If an argument is given, sets the dynamic variable testedModule
    to the given argument. If no argument is given, returns the
    current value of testedModule.
    """
    if module:
        return _environment.tests.let(testedModule = module)
    else:
        return _environment.tests.testedModule

def referenceModule(module = None):
    """
    If an argument is given, sets the dynamic variable referenceModule
    to the given argument. If no argument is given, returns the
    current value of referenceModule.
    """
    if module:
        return _environment.tests.let(referenceModule = module)
    else:
        return _environment.tests.referenceModule
    
def testedFunctionName(functionName = None):
    if functionName:
        @contextmanager
        def context():
            with _environment.tests.let(testedFunctionName = functionName), \
                 condition(runIfFunctionExists(functionName)):
                yield

        return context()
    else:
        return _environment.tests.testedFunctionName

def testedFunction():
    """
    Fetches the tested function.
    """
    return getattr(_environment.tests.testedModule, _environment.tests.testedFunctionName)

def referenceFunction():
    """
    Fetches the reference function.
    """
    return getattr(_environment.tests.referenceModule, _environment.tests.testedFunctionName)

def context(message, *args, **kwargs):
    return _environment.tests.let(context = _environment.tests.context + [ message.format(*args, **kwargs) ])

def path(name, *args, **kwargs):
    return _environment.tests.let(path = _environment.tests.path + "/" + name.format(*args, **kwargs))

def condition(predicate):
    """
    Adds an extra condition which needs to hold true
    for tests to be ran.
    """
    
    # Create conjunction of existing condition with new condition
    conjunction = _environment.tests.condition & predicate

    # Update condition dynamic variable
    return _environment.tests.let(condition = conjunction)

def test(name, *args, **kwargs):
    """
    Decorator that turns the function into a test
    and adds it to the top test's children.
    """
    def wrapper(function):
        # Add test function as child to top test
        _environment.tests.top.addChild(_TestFunction(name.format(*args, **kwargs), function))
        return _dummy

    return wrapper


#
# Assertions
#

def fail():
    """
    When called within a test, aborts the test immediately.
    The test is considered to have failed.
    """
    printer = _environment.settings.printer
    
    printer.log(1, "FAIL: {}", _environment.tests.testName)

#    errorStackFrame = _firstExternalStackFrame()
#    kwargs = { 'file': errorStackFrame.filename, 'line': errorStackFrame.lineno, 'function': errorStackFrame.function }

#    printer.log(2, "In function {function} ({file}, line {line}): {code}", code='<unknown>', **kwargs)

    printer.log(2, "Additional information:")
    for item in _environment.tests.context:
        printer.log(2, "  " + item)

    printer.log(2, "")

    raise TestFailure()

def mustBeEqual(expected, actual):
    """
    Assert that the given values must be equal to each other.
    If they are not, failure ensues.
    """
    with context("Expected value: {}", expected), context("Actual value: {}", actual):
        if expected != actual:
            fail()

def mustBeSameTruthiness(expected, actual):
    """
    Assert that both values represent the same truthiness.
    If they do not, failure ensues.
    """
    if expected:
        with context("Expected {} to be truthy", actual):
            if not actual:
                fail()
    else:
        with context("Expected {} to be falsey", actual):
            if actual:
                fail()
            
def mustBeTruthy(actual):
    """
    Assert that the given value must be truthy.
    If it is not, failure ensues.
    """
    with context("Value that should be true: {}", actual):
        if not actual:
            fail()

def mustBeFalsey(actual):
    """
    Assert that the given value must be falsey.
    If it is not, failure ensues.
    """
    with context("Value that should be false: {}", actual):
        if actual:
            fail()

def ignore(*args, **kwargs):
    """
    Does nothing.
    """
    pass

def reftest(name, result = None, arguments = None):
    compareResults = result or mustBeEqual
    compareArguments = arguments or ignore
    
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
                refretval = referenceFunction()(*refargs, **refkwargs)

                # Call test implementation
                testretval = testedFunction()(*testargs, **testkwargs)

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


@contextmanager
def inside_directory(path):
    currentDirectory = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(currentDirectory)


def loadTests(path):
    with open(path, 'r') as file:
        code = file.read()
        exec(code)

    


def runTests():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', help='Verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-s', '--statistics', help='Statistics verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-n', '--count', help='Number of tests to run', default=float('inf'), type=int)
    args = parser.parse_args()
        
    with _environment.settings.let(printer=_Printer(), verbosity=args.verbosity, maxTests=args.count), \
         _environment.run.let(skipped=[], passed=[], failed=[]):
        printer = _environment.settings.printer
        score = _rootTest.run()

        with _environment.settings.let(verbosity=args.statistics):
            printer.log(1, "Passed tests: {}", len(_environment.run.passed))
            printer.log(1, "Failed tests: {}", len(_environment.run.failed))
            printer.log(1, "Skipped tests: {}", len(_environment.run.skipped))

            printer.log(1, "Score: {}", format(score))


