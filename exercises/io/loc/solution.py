import re
import os


def is_loc(line):
    return re.match(r'\s*[^#\s]', line)


def loc_in_file(filename):
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if is_loc(line):
                count += 1

    return count


def loc_in_directory():
    count = 0
    
    for entry in os.listdir():
        if os.path.isdir(entry):
            os.chdir(entry)
            count += loc_in_directory()
            os.chdir('..')
        elif re.search(r'\.py$', entry):
            count += loc_in_file(entry)

    return count
