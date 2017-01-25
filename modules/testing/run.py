from contextlib import contextmanager
import testing.printers
import testing.tests
import testing.conditions
import testing.printers
import types
import copy
import sys
import os
import dyn




@contextmanager
def inside_directory(path):
    currentDirectory = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(currentDirectory)


def _ensureExistenceOfFile(filename):
    if not os.path.isfile(filename):
        sys.exit('Could not find {} in {}'.format(filename, os.getcwd()))

def _ensureExistenceOfFiles(*filenames):
    for filename in filenames:
        ensureExistenceOfFile(filename)

def _readAndExecuteSourceFile(moduleName, filename):
    module = types.ModuleType(moduleName)

    _ensureExistenceOfFile(filename)
    
    with open(filename, 'r') as file:
        code = file.read()
        exec(code, module.__dict__)

    return module
        
def loadTestsInCurrentDirectory():
    bindings = {}
    
    bindings['testedModule'] = _readAndExecuteSourceFile('student', testing.environment.settings.testedFile)
    
    if os.path.isfile(testing.environment.settings.referenceFile):
        bindings['referenceModule'] =_readAndExecuteSourceFile('solution', testing.environment.settings.referenceFile)

    testModule = types.ModuleType('tests')
    with open('tests.py', 'r') as file, testing.tests.path('tests.py'):
        code = file.read()
        with testing.environment.tests.let( **bindings ):
            exec(code, testModule.__dict__)

def loadTestsRecursively():
    for entry in os.listdir('.'):
        if os.path.isdir(entry):
            with inside_directory(entry), testing.tests.path(entry):
                loadTestsRecursively()
                
    if os.path.isfile('tests.py'):
        loadTestsInCurrentDirectory()

            
def runTests():
    root = testing.environment.tests.top

    if root.childCount() > 0:
        return root.run()
    else:
        print("No tests found!")
        sys.exit(-1)
