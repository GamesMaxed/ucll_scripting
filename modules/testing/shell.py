import argparse
import testing
import testing.run
import testing.tests
import testing.logging
import dyn


def parseSettings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--context', help='Show context', action='store_true')
    parser.add_argument('-s', '--statistics', help='Statistics verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-n', '--count', help='Number of tests to run (default=all tests)', default=float('inf'), type=int)
    parser.add_argument('--test', help='File to be tested (default=student.py)', default='student.py')
    parser.add_argument('--reference', help='Reference implementation file (default=solution.py)', default='solution.py')
    args = parser.parse_args()

    return dict(log=testing.logging.Log(), \
                showContext=args.context, \
                maxTests=args.count, \
                statistics=args.statistics, \
                testedFile=args.test, \
                referenceFile=args.reference)


def printStatistics(score):
    log = testing.environment.log
    message = testing.logging.StatisticsMessage(score, testing.environment.passedTests, testing.environment.failedTests, testing.environment.skippedTests)

    log.write(message)


def main():
    bindings = parseSettings()

    def scoreReceiver(score):
        printStatistics(score)

    bindings['scoreReceiver'] = scoreReceiver
    bindings['skippedTests'] = []
    bindings['passedTests'] = []
    bindings['failedTests'] = []
    bindings['condition'] = testing.conditions.limitTestCount()
    bindings['context'] = []
    bindings['testFilePath'] = []
        
    with testing.environment.let(**bindings), testing.tests.cumulative():
        testing.run.loadTestsRecursively()
