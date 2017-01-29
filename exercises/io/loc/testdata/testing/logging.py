import testing

class Log:
    def write(self, message):
        string = str(message)

        if string:
            print(string)


def log_failure():
    if testing.environment.show_failed_tests:
        print("[FAIL] {}".format("/".join(testing.environment.test_path + [testing.environment.test_description])))

        if testing.environment.show_file_path:
            print("  in file {}".format("/".join(testing.environment.test_file_path)))

        if testing.environment.show_context:
            for entry in testing.environment.context:
                print(str(entry))

def log_success():
    if testing.environment.show_passing_tests:
        print("[PASS] {}".format(testing.environment.test_description))

def log_skip():
    if testing.environment.show_skipped_tests:
        print("[SKIP] {}".format(testing.environment.test_description))

def log_statistics(score):
    print("=" * 50)
    print("#PASS = {}".format(len(testing.environment.passed_tests)))
    print("#FAIL = {}".format(len(testing.environment.failed_tests)))
    print("#SKIP = {}".format(len(testing.environment.skipped_tests)))
    print("SCORE = {}".format(score))

    
