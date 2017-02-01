import zipfile
import re
import os



def read_file(filename):
    with open(filename, 'r') as file:
        return "".join(line for line in file)


def main():
    for filename in os.listdir('.'):
        if re.search(r'\.txt$', filename):
            contents = read_file(filename)

            match = re.search(r'Name: ([a-zA-Z]+) (.*?) \(q(\d+)\)', contents)
            fname = match.group(1)
            lname = match.group(2)

            match = re.search(r'Original filename: ([a-z]+\.zip)', contents)
            original_filename = match.group(1)

            match = re.search(r'Filename: (.*?\.zip)', contents)
            filename = match.group(1)

            slug = "{}-{}".format(re.sub(r'[^a-zA-Z]+', '', lname.lower()), fname.lower())

            os.makedirs(slug)

            with zipfile.ZipFile(filename, 'r') as zip:
                zip.extractall(slug)


try:
    os.chdir('submissions')
    main()
finally:
    os.chdir('..')
    
