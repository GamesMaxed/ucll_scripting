from zipfile import ZipFile
import os


def create_test_data():
    os.mkdir('testdata')

    expected_files = [ 'src/shapes/Shape.java', 'src/shapes/Circle.java', 'src/shapes/Square.java', 'src/App.java' ]
    
    with open('testdata/expected-files.txt', 'w') as file:
        for expected_file in expected_files:
            file.write("{}\n".format(expected_file))
    
    create_zip('testdata/submission1.zip', files=expected_files)
    create_zip('testdata/submission2.zip', files=expected_files)
    create_zip('testdata/submission3.zip', files=expected_files[1:])


def create_zip(path, files):
    with ZipFile(path, 'w') as zip:
        for file in files:
            zip.writestr(file, 'some data')

def main():
    if os.path.exists('testdata'):
        print('Test data already exists; delete it if you want to recreate test data')
    else:
        create_test_data()


if __name__ == '__main__':
    main()
