import testing
import testing.tests


def fail():
    """
    When called within a test, aborts the test immediately.
    The test is considered to have failed.
    """
    testing.logging.logFailure()

    raise testing.tests.TestFailure()

def must_be_equal(expected, actual, epsilon = None):
    """
    Assert that the given values must be equal to each other.
    If they are not, failure ensues.
    """
    if epsilon:
        with testing.tests.context("Expected value: {}", expected), \
             testing.tests.context("Actual value: {}", actual), \
             testing.tests.context("Epsilon: {}", epsilon):
            if abs(expected - actual) > epsilon:
                fail()
    else:
        with testing.tests.context("Expected value: {}", expected), \
             testing.tests.context("Actual value: {}", actual):
            if (not expected == actual) or (expected != actual):
                fail()

def must_not_be_equal(forbidden, actual):
    """
    Assert that the given values must not be equal to each other.
    If they are equal, failure ensues.
    """
    with testing.tests.context("Forbidden alue: {}", forbidden), \
         testing.tests.context("Actual value: {}", actual):
        if not (forbidden != actual) or (forbidden == actual):
            fail()
                
def mustBeSameTruthiness(expected, actual):
    """
    Assert that both values represent the same truthiness.
    If they do not, failure ensues.
    """
    if expected:
        with testing.tests.context("Expected truthy value; got {}", actual):
            if not actual:
                fail()
    else:
        with testing.tests.context("Expected falsey value; got {}", actual):
            if actual:
                fail()
            
def mustBeTruthy(actual):
    """
    Assert that the given value must be truthy.
    If it is not, failure ensues.
    """
    with testing.tests.context("Value that should be true: {}", actual):
        if not actual:
            fail()

def mustBeFalsey(actual):
    """
    Assert that the given value must be falsey.
    If it is not, failure ensues.
    """
    with testing.tests.context("Value that should be false: {}", actual):
        if actual:
            fail()

def mustRaise(exceptionType, code):
    """
    Assert that the execution of the given code
    leads to an exception of the given type.
    """    
    try:
        code()
        with testing.tests.context("No exception thrown; expected exception {}", exceptionType):
            fail()
    except Exception as e:
        if type(e) != exceptionType:
            with testing.tests.context("Wrong exception thrown, expected {}, got {}", exceptionType.__name__, type(e).__name__):
                fail()

def mustContainSameElements(expected, actual, sameOrder=True):
    expected = list(expected)
    actual = list(actual)
    
    with testing.tests.context('Comparing number of elements'):
        must_be_equal(len(expected), len(actual))

    if sameOrder:
        for i in range(0, len(expected)):
            with testing.tests.context('Comparing elements at index {}', i):
                must_be_equal(expected[i], actual[i])
    else:
        for x in expected:
            with testing.tests.context('Looking for element {}', x):
                if x not in actual:
                    fail()
                else:
                    actual.remove(x)
                
                
def ignore(*args, **kwargs):
    """
    Does nothing.
    """
    pass
