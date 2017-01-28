from contextlib import contextmanager
import testing
import testing.conditions
import testing.score
import testing.assertions
import copy


class TestError(Exception):
    def __init__(self, message):
        super().__init__(message)

class TestFailure(TestError):
    def __init__(self):
        super().__init__("Failing assertion")

class InvalidTestCallError(TestError):
    def __init__(self):
        super().__init__("Calling test functions is disallowed")

class Test:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def runTest(self):
        return self.function()


def _runTest(testFunction):
    if not testing.environment.condition():
        # Add current test to skip list
        testing.environment.skippedTests.append(testing.environment.testDescription)

        testing.environment.log.write(2, "SKIP: {}", testing.environment.testDescription)

        # Score 0/1
        testing.environment.scoreReceiver( testing.score.Score(0, 1) )
    else:
        try:
            try:
                # Run test
                testFunction()

                # Add test to pass list
                testing.environment.passedTests.append(testing.environment.testDescription)

                # Score 1/1
                testing.environment.scoreReceiver(testing.score.Score(1, 1))

            except TestFailure as e:
                raise e
            except Exception as e:
                # If a different exception was raised, convert it to a TestFailure exception
                if str(e):
                    contextString = "Exception {} raised: {}".format(type(e).__name__, str(e))
                else:
                    contextString = "Exception {} raised".format(type(e).__name__)

                with context(contextString):
                    testing.assertions.fail()

        except TestFailure:
            # Add test to fail list
            testing.environment.failedTests.append(testing.environment.testDescription)

            # Score 0/1
            testing.environment.scoreReceiver(testing.score.Score(0, 1))
    
    

def test(description, *args, **kwargs):
    description = description.format(*args, **kwargs)
    
    def functionReceiver(testFunction):
        with testing.environment.let(testDescription = description):
            _runTest(testFunction)
            
    return functionReceiver


@contextmanager
def cumulative(skipAfterFail = False):
    total = testing.score.Score(0, 0)

    if skipAfterFail:
        def conditionFunction():
            return total.isMaxScore()

        condition = testing.conditions.fromLambda('skip after first failure', conditionFunction)
    else:
        condition = testing.conditions.runAlways

    def scoreReceiver(score):
        nonlocal total
        total += score

    with testing.environment.let(condition=condition, scoreReceiver=scoreReceiver):
        yield

    testing.environment.scoreReceiver(total)

@contextmanager
def allOrNothing(skipAfterFail = False):
    receivedScore = testing.score.Score(0, 0)
    
    def scoreReceiver(score):
        nonlocal receivedScore
        receivedScore = score

    with testing.environment.let(scoreReceiver=scoreReceiver):
        yield

    if receivedScore.isMaxScore():
        testing.environment.scoreReceiver(testing.score.Score(1, 1))
    else:
        testing.environment.scoreReceiver(testing.score.Score(0, 1))

    
@contextmanager
def context(contextString, *args, **kwargs):
    contextString = contextString.format(*args, **kwargs)
    
    with testing.environment.let(context=testing.environment.context + [contextString]):
        yield

def testedModule(module = None):
    """
    If an argument is given, sets the dynamic variable testedModule
    to the given argument. If no argument is given, returns the
    current value of testedModule.
    """
    if module:
        return testing.environment.let(testedModule = module)
    else:
        return testing.environment.testedModule

def referenceModule(module = None):
    """
    If an argument is given, sets the dynamic variable referenceModule
    to the given argument. If no argument is given, returns the
    current value of referenceModule.
    """
    if module:
        return testing.environment.let(referenceModule = module)
    else:
        return testing.environment.referenceModule
    
def testedFunctionName(functionName = None):
    if functionName:
        @contextmanager
        def context():
            with testing.environment.let(testedFunctionName = functionName), \
                 condition(testing.conditions.runIfFunctionExists(functionName)):
                yield

        return context()
    else:
        return testing.environment.testedFunctionName

def _getTestedFunction():
    """
    Fetches the test function.
    """
    return getattr(testing.environment.testedModule, testing.environment.testedFunctionName)

def _getReferenceFunction():
    """
    Fetches the test function.
    """
    return getattr(testing.environment.referenceModule, testing.environment.testedFunctionName)

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
        
def condition(cond = None):
    """
    Adds an extra condition which needs to hold true
    for tests to be ran.
    """

    if cond:    
        # Create conjunction of existing condition with new condition
        conjunction = testing.environment.condition & cond

        # Update condition dynamic variable
        return testing.environment.let(condition = conjunction)
    else:
        return testing.environment.condition

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

@contextmanager
def scale(maximum):
    currentScoreReceiver = testing.environment.scoreReceiver
    
    def scoreReceiver(score):
        currentScoreReceiver(score.rescale(maximum))

    with testing.environment.let(scoreReceiver=scoreReceiver):
        yield
