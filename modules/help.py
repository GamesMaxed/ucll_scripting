import fileutil
import sys
import os


def print_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            for line in file:
                print(line.rstrip())
                

def find_readme():
    if os.path.isfile('readme.txt'):
        return os.path.abspath('readme.txt')
    elif os.path.isdir('.git'):
        return None
    else:
        with fileutil.inside_directory('..'):
            return find_readme()


def main():
    path = find_readme()

    if path:
        print_file(path)        
    else:
        sys.exit('No readme.txt found!')


if __name__ == '__main__':
    main()
