import testing


class _TestCondition:
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
        return _TestCondition( "{} & {}".format(str(self), str(other)), check )

    def __str__(self):
        return self._name


runAlways = _TestCondition("always", lambda: True)

runNever = _TestCondition("never", lambda: False)

def runIfFunctionExists(functionName):
    if not testing.environment.tests.isBound('testedModule'):
        raise testing.tests.TestError("No tested module set")
    else:
        def check():
            return functionName in dir(testing.environment.tests.testedModule)
        
        return _TestCondition("run if {} exists".format(functionName), check)


def limitTestCount():
    def check():
        return len(testing.environment.run.passed) + len(testing.environment.run.failed) < testing.environment.settings.maxTests

    return _TestCondition("limit test count", check)
