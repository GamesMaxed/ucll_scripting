from contextlib import contextmanager
import testing.tests
import testing.conditions
import testing.logging
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


def _ensure_existence_of_file(filename):
    if not os.path.isfile(filename):
        sys.exit('Could not find {} in {}'.format(filename, os.getcwd()))

def _ensure_existence_of_files(*filenames):
    for filename in filenames:
        ensureExistenceOfFile(filename)

def _read_and_execute_source_file(moduleName, filename):
    module = types.ModuleType(moduleName)

    _ensure_existence_of_file(filename)
    
    with open(filename, 'r') as file:
        code = file.read()
        exec(code, module.__dict__)

    return module
        
def load_tests_in_current_directory():
    bindings = {}
    
    bindings['tested_module'] = _read_and_execute_source_file('student', testing.environment.testedFile)
    
    if os.path.isfile(testing.environment.referenceFile):
        bindings['reference_module'] =_read_and_execute_source_file('solution', testing.environment.referenceFile)

    testModule = types.ModuleType('tests')
    with open('tests.py', 'r') as file:
        code = file.read()
        with testing.environment.let( **bindings ):
            exec(code, testModule.__dict__)

def load_tests_recursively():
    for entry in os.listdir('.'):
        if os.path.isdir(entry):
            with inside_directory(entry), test_file_path(entry):
                load_tests_recursively()
                
    if os.path.isfile('tests.py'):
        with test_file_path('tests.py'):
            load_tests_in_current_directory()

@contextmanager
def test_file_path(component):
    oldPath = testing.environment.test_file_path
    
    with testing.environment.let(test_file_path = oldPath + [ component ]):
        yield
