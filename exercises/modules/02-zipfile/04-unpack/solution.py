from zipfile import ZipFile
import sys
import os
import re


def find_files_with_extension(extension):
    return [ file for file in os.listdir('.') if file.endswith(extension) ]


def get_id_from_filename(filename):
    return re.search(r'-(q\d+)-', filename).group(1)


def collect_slugs():
    result = {}

    for file in find_files_with_extension('.txt'):
        id = get_id_from_filename(file)

        with open(file, 'r') as f:
            match = re.search(r'Name: (.*?) (.*)', f.read())

            fname = match.group(1)
            lname = match.group(2)
            slug = lname.replace(' ', '-').lower() + '-' + fname.lower()

            result[id] = slug

    return result
            
    

def main():
    os.chdir(sys.argv[1])
    
    table = collect_slugs()
    
    for zipfilename in find_files_with_extension('.zip'):
        id = get_id_from_filename(zipfilename)
        slug = table[id]
        
        with ZipFile(zipfilename) as zip:
            zip.extractall(slug)


if __name__ == '__main__':
    main()
