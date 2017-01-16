import inspect
import copy
import sys
import dyn


def checkPythonVersion():
    version = sys.version_info

    if version.major < 3 or (version.major == 3 and version.minor < 5):
        sys.exit("You need at least Python 3.5")

checkPythonVersion()
        
class TestError(Exception):
    def __init__(self, message):
        super().__init__(message)

class TestFailure(TestError):
    def __init__(self):
        super().__init__("Failing assertion")

class InvalidTestCallError(TestError):
    def __init__(self):
        super().__init__("Calling test functions is disallowed")
        
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
        self._environment = _testenv.copy()

    def run(self):
        global _testenv

        if self._environment.skip:
            self._environment.skippedTests.append(self._name)
        else:
            oldTestEnv = _testenv
            try:
                _testenv = self._environment
                _testenv.push(testName = self._name)
                self._function()
                self._environment.passedTests.append(self._name)
                return Score(1, 1)
            except TestFailure:
                self._environment.failedTests.append(self._name)
                return Score(0, 1)
            finally:
                _testenv = oldTestEnv


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


# Create root test
_rootTest = _RootTest()

# Create separate dynamic environment for tests
_testenv = dyn.create()

# Push a fresh frame with the root test in it
# (necessary due to the root frame not being modifiable)
_testenv.push(top=_rootTest, context=[], passedTests=[], failedTests=[], skippedTests=[], skip=False)


def _dummy():
    raise InvalidTestCallError()


class _TestContextManager:
    def __init__(self, *tests):
        super().__init__()
        self._tests = tests
        
    def __enter__(self):
        for test in self._tests:
            _testenv.top.addChild(test)
            _testenv.push(top=test)

    def __exit__(self, *args):
        for test in self._tests:
            _testenv.pop()


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
    return findFirst(inspect.stack(), lambda frame: frame.filename != __file__)
        

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
        return _testenv.let(testedModule = module)
    else:
        return _testenv.testedModule

def referenceModule(module = None):
    """
    If an argument is given, sets the dynamic variable referenceModule
    to the given argument. If no argument is given, returns the
    current value of referenceModule.
    """
    if module:
        return _testenv.let(referenceModule = module)
    else:
        return _testenv.referenceModule
    
def testedFunctionName(functionName = None):
    """
    If an argument is given, sets the dynamic variables testedFunctionName
    to the given argument. It also sets testedFunction and referenceFunction by looking
    it up in the current testedModule and referenceModule, respectively.
    If no referenceModule is set, referenceFunction remains unmodified.

    If no argument is given, returns the
    current value of testedFunctionName.
    """
    if functionName:
        bindings = { "testedFunctionName": functionName }
        
        assert _testenv.testedModule, "No testedModule set!"
        bindings["testedFunction"] = getattr(_testenv.testedModule, functionName)
        
        # Only set referenceFunction if referenceModule is set
        if _testenv.isBound("referenceModule"):
            bindings["referenceFunction"] = getattr(_testenv.referenceModule, functionName)

        return _testenv.let(**bindings)
    else:
        return _testenv.testedFunctionName

def testedFunction():
    return _testenv.testedFunction

def referenceFunction():
    return _testenv.referenceFunction

def context(message, *args, **kwargs):
    return _testenv.let(context = _testenv.context + [ message.format(*args, **kwargs) ])

def test(name, *args, **kwargs):
    """
    Decorator that turns the function into a test
    and adds it to the top test's children.
    """
    def wrapper(function):
        # Add test function as child to top test
        _testenv.top.addChild(_TestFunction(name.format(*args, **kwargs), function))
        return _dummy

    return wrapper


def fail():
    errorStackFrame = _firstExternalStackFrame()

    print("FAIL: {}".format(_testenv.testName))
    
    if len(errorStackFrame.code_context) > 1:
        print("FAIL: {}".format(_testenv.testName))
        print("In function {function} ({file}, line {line}):".format(file = errorStackFrame.filename, line = errorStackFrame.lineno, function = errorStackFrame.function))
        print("\n".join([ "  " + line.strip() for line in errorStackFrame.code_context ]))
    else:
        print("In function {function} ({file}, line {line}): {code}".format(file = errorStackFrame.filename, line = errorStackFrame.lineno, function = errorStackFrame.function, code = errorStackFrame.code_context[0].strip()))

    print("Additional information:")
    for item in _testenv.context:
        print("  " + item)

    print("")
    raise TestFailure()

def mustBeEqual(expected, actual):
    with context("Expected value: {}", expected), context("Actual value: {}", actual):
        if expected != actual:
            fail()

def mustBeSameTruthiness(expected, actual):
    if expected:
        with context("Expected {} to be truthy", actual):
            if not actual:
                fail()
    else:
        with context("Expected {} to be falsey", actual):
            if actual:
                fail()
            
def mustBeTruthy(actual):
    with context("Value that should be true: {}", actual):
        if not actual:
            fail()

def mustBeFalsey(actual):
    with context("Value that should be false: {}", actual):
        if actual:
            fail()

def ignore(*args, **kwargs):
    pass

            
def reftest(name, result = None, arguments = None):
    compareResults = result or mustBeEqual
    compareArguments = arguments or ignore
    
    def testFunction(*args, **kwargs):
        assert _testenv.isBound("testedFunction"), "No test function set. Use testedModule and testedFunctionName."
        assert _testenv.isBound("referenceFunction"), "No reference function set. Use referenceModule and testedFunctionName."
    
        @test(name)
        def referenceImplementationTest():
            testargs = copy.deepcopy(args)
            testkwargs = copy.deepcopy(kwargs)
            refargs = copy.deepcopy(args)
            refkwargs = copy.deepcopy(kwargs)

            refretval = _testenv.referenceFunction(*refargs, **refkwargs)
            testretval = _testenv.testedFunction(*testargs, **testkwargs)

            with context("Comparing return values"):
                compareResults(refretval, testretval)

            for i in range(0, len(args)):
                with context("Comparing positional argument #{}", i):
                    compareArguments(refargs[i], testargs[i])

            for key in kwargs:
                with context("Comparing keyword argument {}", key):
                    compareArguments(refkwargs[key], testkwargs[i])

    return testFunction
            
            
def runTests():
    score = _testenv.top.run()
    print("Passed tests: {}".format(len(_testenv.passedTests)))
    print("Failed tests: {}".format(len(_testenv.failedTests)))
    print("Skipped tests: {}".format(len(_testenv.skippedTests)))
    print("Score: {}".format(score))

