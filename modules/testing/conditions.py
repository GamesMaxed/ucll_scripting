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

def run_if_exists(identifier):
    if 'tested_module' not in testing.environment:
        raise testing.tests.TestError("No tested module set")
    else:
        def check():
            return identifier in dir(testing.environment.tested_module)

        return TestCondition("run if {} exists".format(identifier), check)
    

def run_if_function_exists(function_name):
    return run_if_exists(function_name) & from_lambda('{} is a function'.format(function_name), lambda: callable(getattr(testing.environment.tested_module, function_name)))

def run_if_class_exists(class_name):
    return run_if_exists(class_name) & from_lambda('{} is a class'.format(class_name), lambda: type(getattr(testing.environment.tested_module, class_name)) == type)

def limit_test_count():
    def check():
        return len(testing.environment.passed_tests) + len(testing.environment.failed_tests) < testing.environment.max_tests

    return TestCondition("limit test count", check)

def from_lambda(name, function):
    return TestCondition(name, function)
