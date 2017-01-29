import testing

class Log:
    def write(self, message):
        string = str(message)

        if string:
            print(string)


def log_failure():
    if testing.environment.showFailedTests:
        print("[FAIL] {}".format("/".join(testing.environment.testPath + [testing.environment.testDescription])))

        if testing.environment.showFilePath:
            print("  in file {}".format("/".join(testing.environment.test_file_path)))

        if testing.environment.showContext:
            for entry in testing.environment.context:
                print(str(entry))

def log_success():
    if testing.environment.showPassingTests:
        print("[PASS] {}".format(testing.environment.testDescription))

def log_skip():
    if testing.environment.showSkippedTests:
        print("[SKIP] {}".format(testing.environment.testDescription))

def log_statistics(score):
    print("=" * 50)
    print("#PASS = {}".format(len(testing.environment.passedTests)))
    print("#FAIL = {}".format(len(testing.environment.failedTests)))
    print("#SKIP = {}".format(len(testing.environment.skippedTests)))
    print("SCORE = {}".format(score))

    
