import argparse
import testing
import testing.run
import testing.tests
import testing.printers
import dyn


def parseSettings():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', help='Verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-s', '--statistics', help='Statistics verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-n', '--count', help='Number of tests to run (default=all tests)', default=float('inf'), type=int)
    parser.add_argument('--test', help='File to be tested (default=student.py)', default='student.py')
    parser.add_argument('--reference', help='Reference implementation file (default=solution.py)', default='solution.py')
    args = parser.parse_args()

    return dict(printer=testing.printers.Printer(), \
                verbosity=args.verbosity, \
                maxTests=args.count, \
                statistics=args.statistics, \
                testedFile=args.test, \
                referenceFile=args.reference)


def printStatistics(score):
    printer = testing.environment.settings.printer

    with testing.environment.settings.let(verbosity=testing.environment.statistics):
        printer.log(1, "Passed tests: {}", len(testing.environment.run.passed))
        printer.log(2, "\n".join("  " + test for test in testing.environment.passed))
        printer.log(1, "Failed tests: {}", len(testing.environment.run.failed))
        printer.log(2, "\n".join("  " + test for test in testing.environment.failed))
        printer.log(1, "Skipped tests: {}", len(testing.environment.run.skipped))
        printer.log(2, "\n".join("  " + test for test in testing.environment.skipped))
        
        printer.log(1, "Score: {}", format(score))


def main():
    bindings = parseSettings()

    # with testing.environment.let(tests = dyn.create(), settings = dyn.create(), run = dyn.create()), \
    #      testing.environment.tests.let(top=root, context=[], path="", condition = testing.conditions.limitTestCount()), \
    #      testing.environment.settings.let( **settings ), \
    #      testing.environment.run.let(skipped=[], passed=[], failed=[], condition = testing.conditions.runAlways):
    #     testing.run.loadTestsRecursively()
    #     score = testing.run.runTests()
    #     printStatistics(score)

    def scoreReceiver(score):
        print("Received score {}".format(score))

    bindings['scoreReceiver'] = scoreReceiver
    bindings['skippedTests'] = []
    bindings['passedTests'] = []
    bindings['failedTests'] = []
    bindings['condition'] = testing.conditions.limitTestCount()
    bindings['context'] = []
    
        
    with testing.environment.let(**bindings), testing.tests.cumulative():
        testing.run.loadTestsRecursively()
