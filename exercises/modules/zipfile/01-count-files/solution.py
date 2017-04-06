from zipfile import ZipFile
import sys


def count_files_in_zip(path):
    with ZipFile(path) as zip:
        return len(zip.namelist())


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print("{} {}".format(path, count_files_in_zip(path)))
