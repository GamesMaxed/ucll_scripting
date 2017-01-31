from contextlib import contextmanager
import os


@contextmanager
def inside_directory(path):
    current_directory = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(current_directory)
