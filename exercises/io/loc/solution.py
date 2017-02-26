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


def loc_in_directory(path):
    count = 0
    
    for entry in os.scandir(path):
        if entry.is_dir():
            count += loc_in_directory(entry.path)
        elif re.search(r'\.py$', entry.name):
            count += loc_in_file(entry.path)

    return count
