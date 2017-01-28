import testing

class Log:
    def write(self, message):
        string = str(message)

        if string:
            print(string)


class TestFailureMessage:
    def __init__(self, testDescription, context):
        self.testDescription = testDescription
        self.context = context

    def __str__(self):
        result = "[FAIL] {}".format(self.testDescription)
        
        if testing.environment.showContext:
            result = "\n".join( [result] + [str(entry) for entry in self.context] )

        return result


class StatisticsMessage:
    def __init__(self, score, passedTests, failedTests, skippedTests):
        self.score = score
        self.passedTests = passedTests
        self.failedTests = failedTests
        self.skippedTests = skippedTests

    def __str__(self):
        result = "=" * 50 + "\n"
        result += "#PASS = {}\n".format(len(self.passedTests))
        result += "#FAIL = {}\n".format(len(self.failedTests))
        result += "#SKIP = {}\n".format(len(self.skippedTests))
        result += "SCORE = {}".format(self.score)

        return result
