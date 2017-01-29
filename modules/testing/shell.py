import argparse
import testing
import testing.run
import testing.tests
import testing.logging
import dyn


def parse_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--show-context', help='Show context', action='store_true')
    parser.add_argument('-n', '--count', help='Number of tests to run (default=all tests)', default=float('inf'), type=int)
    parser.add_argument('--test', help='File to be tested (default=student.py)', default='student.py')
    parser.add_argument('--reference', help='Reference implementation file (default=solution.py)', default='solution.py')
    parser.add_argument('--show-pass', help='Shows passing tests', action='store_true')
    parser.add_argument('--show-skip', help='Shows skipped tests', action='store_true')
    parser.add_argument('--hide-fail', help='Hides failed tests', action='store_true')
    parser.add_argument('--show-filepath', help='Shows path of tests.py', action='store_true')
    args = parser.parse_args()

    return dict(log=testing.logging.Log(), \
                showContext=args.show_context, \
                maxTests=args.count, \
                testedFile=args.test, \
                showPassingTests=args.show_pass, \
                showSkippedTests=args.show_skip, \
                showFailedTests=not args.hide_fail, \
                showFilePath=args.show_filepath, \
                referenceFile=args.reference)


def main():
    bindings = parse_settings()

    def score_receiver(score):
        testing.logging.log_statistics(score)

    bindings['score_receiver'] = score_receiver
    bindings['skippedTests'] = []
    bindings['passedTests'] = []
    bindings['failedTests'] = []
    bindings['condition'] = testing.conditions.limit_test_count()
    bindings['context'] = []
    bindings['testPath'] = []
    bindings['test_file_path'] = []
        
    with testing.environment.let(**bindings), testing.tests.cumulative():
        testing.run.load_tests_recursively()
