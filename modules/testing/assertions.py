import testing
import testing.tests


def fail():
    """
    When called within a test, aborts the test immediately.
    The test is considered to have failed.
    """
    testing.logging.log_failure()

    raise testing.tests.TestFailure()


class MustBeEqualAssertion:
    def with_epsilon(self, epsilon):
        return MustBeEqualWithEpsilonAssertion(epsilon)

    def __call__(self, expected, actual):
        with testing.tests.context("Expected value: {}", expected), \
             testing.tests.context("Actual value: {}", actual):
            if (not expected == actual) or (expected != actual):
                fail()
        

class MustBeEqualWithEpsilonAssertion:        
    def __init__(self, epsilon):
        self._epsilon = epsilon

    def __call__(self, expected, actual):
        with testing.tests.context("Expected value: {}", expected), \
             testing.tests.context("Actual value: {}", actual), \
             testing.tests.context("Epsilon: {}", self._epsilon):
            if abs(expected - actual) > self._epsilon:
                fail()


must_be_equal = MustBeEqualAssertion()


def must_not_be_equal(forbidden, actual):
    """
    Assert that the given values must not be equal to each other.
    If they are equal, failure ensues.
    """
    with testing.tests.context("Forbidden alue: {}", forbidden), \
         testing.tests.context("Actual value: {}", actual):
        if not (forbidden != actual) or (forbidden == actual):
            fail()
                
def must_be_same_truthiness(expected, actual):
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
            
def must_be_truthy(actual):
    """
    Assert that the given value must be truthy.
    If it is not, failure ensues.
    """
    with testing.tests.context("Value that should be true: {}", actual):
        if not actual:
            fail()

def must_be_falsey(actual):
    """
    Assert that the given value must be falsey.
    If it is not, failure ensues.
    """
    with testing.tests.context("Value that should be false: {}", actual):
        if actual:
            fail()

def must_raise(exception_type, code):
    """
    Assert that the execution of the given code
    leads to an exception of the given type.
    """    
    try:
        code()
        with testing.tests.context("No exception thrown; expected exception {}", exception_type.__name__):
            fail()
    except testing.tests.TestFailure as e:
        raise e
    except Exception as e:
        if type(e) != exception_type:
            with testing.tests.context("Wrong exception thrown, expected {}, got {}", exception_type.__name__, type(e).__name__):
                fail()

def must_contain_same_elements(expected, actual, same_order=True):
    expected = list(expected)
    actual = list(actual)

    with testing.tests.context('{} must contain same elements as {}', expected, actual):
        with testing.tests.context('Comparing number of elements'):
            must_be_equal(len(expected), len(actual))

        if same_order:
            for i in range(0, len(expected)):
                with testing.tests.context('Comparing elements at index {}', i):
                    must_be_equal(expected[i], actual[i])
        else:
            for x in expected:
                with testing.tests.context('{} should be in {}', x, actual):
                    if x not in actual:
                        fail()
                    else:
                        actual.remove(x)

def must_be_element(permissible_values, value):
    with testing.tests.context('{} must be member of {}', value, permissible_values):
        if value not in permissible_values:
            fail()
                        
def ignore(*args, **kwargs):
    """
    Does nothing.
    """
    pass
