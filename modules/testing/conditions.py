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

def runIfFunctionExists(functionName):
    if not testing.environment.isBound('testedModule'):
        raise testing.tests.TestError("No tested module set")
    else:
        def check():
            return functionName in dir(testing.environment.testedModule)
        
        return TestCondition("run if {} exists".format(functionName), check)

def limitTestCount():
    def check():
        return len(testing.environment.passedTests) + len(testing.environment.failedTests) < testing.environment.maxTests

    return TestCondition("limit test count", check)

def fromLambda(name, function):
    return TestCondition(name, function)
