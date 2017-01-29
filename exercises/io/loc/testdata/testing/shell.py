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
                show_context=args.show_context, \
                max_tests=args.count, \
                tested_file=args.test, \
                show_passing_tests=args.show_pass, \
                show_skipped_tests=args.show_skip, \
                show_failed_tests=not args.hide_fail, \
                show_file_path=args.show_filepath, \
                reference_file=args.reference)


def main():
    bindings = parse_settings()

    def score_receiver(score):
        testing.logging.log_statistics(score)

    bindings['score_receiver'] = score_receiver
    bindings['skipped_tests'] = []
    bindings['passed_tests'] = []
    bindings['failed_tests'] = []
    bindings['condition'] = testing.conditions.limit_test_count()
    bindings['context'] = []
    bindings['test_path'] = []
    bindings['test_file_path'] = []
        
    with testing.environment.let(**bindings), testing.tests.cumulative():
        testing.run.load_tests_recursively()
