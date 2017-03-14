import sys
import re
import os



comment_delimiters = { '.py': '#',
                       '.cpp': '//',
                       '.java': '//',
                       '.rb': '#',
                       '.cl': '%',
                       '.tex': '%',
                       '.hs': '--' }


def is_loc(line, comment_delimiter):
    line = line.lstrip()
    return len(line) > 0 and not line.startswith(comment_delimiter)


def extension_of(filename):
    return os.path.splitext(filename)[1]
    

def is_source_file(filename):
    return extension_of(filename) in comment_delimiters


def comment_delimiter_for(filename):
    return comment_delimiters[extension_of(filename)]


def loc(source, delimiter):
    return sum( 1 for line in source.split("\n") if is_loc(line, delimiter) )


def loc_in_file(filename):
    if is_source_file(filename):        
        with open(filename, 'r') as file:
            return loc(file.read(), comment_delimiter_for(filename))
    else:
        return 0   


def loc_in_directory(path):
    return sum( loc_in_directory(entry.path) if entry.is_dir() else loc_in_file(entry.path) for entry in os.scandir(path) )


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = '.'

    print(loc_in_directory(path))
