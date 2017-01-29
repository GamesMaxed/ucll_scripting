import testing


class TestCondition:
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
            return self() and other()
        return TestCondition( "{} & {}".format(str(self), str(other)), check )

    def __str__(self):
        return self._name


runAlways = TestCondition("always", lambda: True)

runNever = TestCondition("never", lambda: False)

def run_if_function_exists(functionName):
    if not testing.environment.is_bound('tested_module'):
        raise testing.tests.TestError("No tested module set")
    else:
        def check():
            return functionName in dir(testing.environment.tested_module)
        
        return TestCondition("run if {} exists".format(functionName), check)

def limit_test_count():
    def check():
        return len(testing.environment.passedTests) + len(testing.environment.failedTests) < testing.environment.maxTests

    return TestCondition("limit test count", check)

def from_lambda(name, function):
    return TestCondition(name, function)
