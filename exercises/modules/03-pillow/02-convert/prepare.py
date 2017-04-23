import zipfile
import urllib.request
import os


def create_test_data():
    print('Creating directory testdata')
    os.mkdir('testdata')

    print('Downloading images.zip')
    urllib.request.urlretrieve('http://alexander.khleuven.be/courses/scripting/extra/images.zip', filename='testdata/images.zip')

    print('Unzipping images.zip')
    with zipfile.ZipFile('testdata/images.zip') as zip:
        zip.extractall('testdata')

    print('Deleting zip')
    os.remove('testdata/images.zip')
        


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
