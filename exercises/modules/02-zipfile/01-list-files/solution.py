from zipfile import ZipFile
import sys


def print_files_in_zip(path):
    with ZipFile(path) as zip:
        for name in zip.namelist():
            print(name)


if __name__ == '__main__':
    print_files_in_zip(sys.argv[1])
