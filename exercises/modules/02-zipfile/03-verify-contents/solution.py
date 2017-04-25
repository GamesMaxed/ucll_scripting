from zipfile import ZipFile
import argparse
import sys



def verify(zipfile, expected_files):
    with ZipFile(zipfile) as zip:
        zip_contents = set(zip.namelist())

    missing_files = expected_files - zip_contents

    if missing_files:
        print("{} is missing {}".format(zipfile, ",".join(str(missing_file) for missing_file in missing_files)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('zipfiles', nargs='+')
    parser.add_argument('--expected-files', required=True)
    args = parser.parse_args()

    with open(args.expected_files, 'r') as file:
        expected_files = set( line.strip() for line in file )
    
    for zipfile in args.zipfiles:
        verify(zipfile, expected_files)


if __name__ == '__main__':
    main()
