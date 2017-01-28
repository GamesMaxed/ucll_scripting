import argparse
import testing
import testing.run
import testing.tests
import testing.logging
import dyn


def parseSettings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--context', help='Show context', action='store_true')
    parser.add_argument('-n', '--count', help='Number of tests to run (default=all tests)', default=float('inf'), type=int)
    parser.add_argument('--test', help='File to be tested (default=student.py)', default='student.py')
    parser.add_argument('--reference', help='Reference implementation file (default=solution.py)', default='solution.py')
    parser.add_argument('--show-pass', help='Shows passing tests', action='store_true')
    parser.add_argument('--show-skip', help='Shows skipped tests', action='store_true')
    parser.add_argument('--show-filepath', help='Shows path of tests.py', action='store_true')
    args = parser.parse_args()

    return dict(log=testing.logging.Log(), \
                showContext=args.context, \
                maxTests=args.count, \
                testedFile=args.test, \
                showPassingTests=args.show_pass, \
                showSkippedTests=args.show_skip, \
                showFilePath=args.show_filepath, \
                referenceFile=args.reference)


def main():
    bindings = parseSettings()

    def scoreReceiver(score):
        testing.logging.logStatistics(score)

    bindings['scoreReceiver'] = scoreReceiver
    bindings['skippedTests'] = []
    bindings['passedTests'] = []
    bindings['failedTests'] = []
    bindings['condition'] = testing.conditions.limitTestCount()
    bindings['context'] = []
    bindings['testPath'] = []
    bindings['testFilePath'] = []
        
    with testing.environment.let(**bindings), testing.tests.cumulative():
        testing.run.loadTestsRecursively()
