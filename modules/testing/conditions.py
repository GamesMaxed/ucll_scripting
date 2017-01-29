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


run_always = TestCondition("always", lambda: True)

run_never = TestCondition("never", lambda: False)

def run_if_function_exists(function_name):
    if not testing.environment.is_bound('tested_module'):
        raise testing.tests.TestError("No tested module set")
    else:
        def check():
            return function_name in dir(testing.environment.tested_module)
        
        return TestCondition("run if {} exists".format(function_name), check)

def limit_test_count():
    def check():
        return len(testing.environment.passed_tests) + len(testing.environment.failed_tests) < testing.environment.max_tests

    return TestCondition("limit test count", check)

def from_lambda(name, function):
    return TestCondition(name, function)
