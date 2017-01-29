from contextlib import contextmanager
import testing
import testing.conditions
import testing.score
import testing.assertions
import copy
import traceback
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

class Test:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def run_test(self):
        return self.function()


def _run_test(test_function):
    if not testing.environment.condition():
        # Add current test to skip list
        testing.environment.skippedTests.append(testing.environment.testDescription)

        # Score 0/1
        testing.environment.score_receiver( testing.score.Score(0, 1) )

        testing.logging.log_skip()
    else:
        try:
            try:
                # Run test
                test_function()

                # Add test to pass list
                testing.environment.passedTests.append(testing.environment.testDescription)

                # Score 1/1
                testing.environment.score_receiver(testing.score.Score(1, 1))

                testing.logging.log_success()

            except TestFailure as e:
                raise e
            except Exception as e:
                # If a different exception was raised, convert it to a TestFailure exception
                exception_type, exception_value, exception_tb = sys.exc_info()
                exception_strings = traceback.format_exception(exception_type, exception_value, exception_tb)
                exception_string = "\n".join(exception_strings[-2:-1])
                
                if str(e):
                    context_string = "Exception {} raised: {}\n{}".format(type(e).__name__, str(e), exception_string)
                else:
                    context_string = "Exception {} raised".format(type(e).__name__)

                with context(context_string):
                    testing.assertions.fail()

        except TestFailure:
            # Add test to fail list
            testing.environment.failedTests.append(testing.environment.testDescription)

            # Score 0/1
            testing.environment.score_receiver(testing.score.Score(0, 1))
    
    

def test(description, *args, **kwargs):
    description = description.format(*args, **kwargs)
    
    def function_receiver(test_function):
        with testing.environment.let(testDescription = description):
            _run_test(test_function)
            
    return function_receiver


@contextmanager
def cumulative(skipAfterFail = False):
    total = testing.score.Score(0, 0)

    if skipAfterFail:
        def condition_function():
            return total.is_max_score()

        condition = testing.conditions.from_lambda('skip after first failure', condition_function)
    else:
        condition = testing.conditions.runAlways

    def score_receiver(score):
        nonlocal total
        total += score

    with testing.environment.let(condition=condition, score_receiver=score_receiver):
        yield

    testing.environment.score_receiver(total)

@contextmanager
def all_or_nothing(skipAfterFail = False):
    receivedScore = testing.score.Score(0, 0)
    
    def score_receiver(score):
        nonlocal receivedScore
        receivedScore = score

    with testing.environment.let(score_receiver=score_receiver):
        yield

    if receivedScore.is_max_score():
        testing.environment.score_receiver(testing.score.Score(1, 1))
    else:
        testing.environment.score_receiver(testing.score.Score(0, 1))

    
@contextmanager
def context(contextString, *args, **kwargs):
    contextString = contextString.format(*args, **kwargs)
    
    with testing.environment.let(context=testing.environment.context + [contextString]):
        yield

def tested_module(module = None):
    """
    If an argument is given, sets the dynamic variable tested_module
    to the given argument. If no argument is given, returns the
    current value of tested_module.
    """
    if module:
        return testing.environment.let(tested_module = module)
    else:
        return testing.environment.tested_module

def reference_module(module = None):
    """
    If an argument is given, sets the dynamic variable reference_module
    to the given argument. If no argument is given, returns the
    current value of reference_module.
    """
    if module:
        return testing.environment.let(reference_module = module)
    else:
        return testing.environment.reference_module
    
def tested_function_name(functionName = None):
    if functionName:
        @contextmanager
        def context():
            with testing.environment.let(tested_function_name = functionName), \
                 condition(testing.conditions.run_if_function_exists(functionName)):
                yield

        return context()
    else:
        return testing.environment.tested_function_name

def _get_tested_function():
    """
    Fetches the test function.
    """
    return getattr(testing.environment.tested_module, testing.environment.tested_function_name)

def _get_reference_function():
    """
    Fetches the test function.
    """
    return getattr(testing.environment.reference_module, testing.environment.tested_function_name)

def tested_function(*args, **kwargs):
    """
    Calls the tested function with the provided arguments.
    """
    return _get_tested_function()(*args, **kwargs)

def reference_function(*args, **kwargs):
    """
    Calls the reference function with the provided arguments.
    """
    return _get_reference_function()(*args, **kwargs)
        
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

def _limit_string_length(string, maxLength = 60):
    if len(string) > maxLength:
        return string[0:maxLength-3] + "..."
    else:
        return string
    
def reftest(result = None, arguments = None):
    compareResults = result or testing.assertions.must_be_equal
    compareArguments = arguments or testing.assertions.ignore
    
    def test_function(*args, **kwargs):
        argumentStrings = [ repr(arg) for arg in args ] + [ "{} = {}".format(key, repr(val)) for key, val in kwargs ]
        argumentString = "{}".format(", ".join(argumentStrings))

        # Call reference function
        refargs = copy.deepcopy(args)
        refkwargs = copy.deepcopy(kwargs)
        refretval = reference_function(*refargs, **refkwargs)

        name = "{}({}), refimpl returned {}".format(tested_function_name(), argumentString, _limit_string_length(str(refretval)))
        
        @test(name)
        def reference_implementation_test():
            with context('Comparing {}({}) with reference solution', tested_function_name(), argumentString):
                # Call test implementation
                testargs = copy.deepcopy(args)
                testkwargs = copy.deepcopy(kwargs)
                testretval = tested_function(*testargs, **testkwargs)

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

    return test_function

@contextmanager
def scale(maximum):
    currentScoreReceiver = testing.environment.score_receiver
    
    def score_receiver(score):
        currentScoreReceiver(score.rescale(maximum))

    with testing.environment.let(score_receiver=score_receiver):
        yield

@contextmanager
def path(component):
    currentPath = testing.environment.testPath

    with testing.environment.let(testPath = currentPath + [ component ]):
        yield
