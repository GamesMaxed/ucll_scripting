from zipfile import ZipFile
import os


def create_test_data():
    os.mkdir('testdata')
    create_zip('testdata/test1.zip', nfiles=5)
    create_zip('testdata/test2.zip', nfiles=11)
    create_zip('testdata/test3.zip', nfiles=29)


def create_zip(path, nfiles):
    with ZipFile(path, 'w') as zip:
        for i in range(nfiles):
            filename = 'file{}.txt'.format(i+1)
            zip.writestr(filename, 'some data')

def main():
    if os.path.exists('testdata'):
        print('Test data already exists; delete it if you want to recreate test data')
    else:
        create_test_data()


if __name__ == '__main__':
    main()
