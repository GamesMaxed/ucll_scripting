from zipfile import ZipFile
import os


def create_test_data():
    os.mkdir('testdata')
    create_submission('Jan', 'Peters', 'q0048766')
    create_submission('Piet', 'Janssens', 'q0011357')
    create_submission('Pieter', 'Cockx', 'q0077161')
    create_submission('Jos', 'Van den Bergh', 'q0077161')


def create_submission(fname, lname, id):
    def create_zipfile(path):
        with ZipFile(path, 'w') as zip:
                for i in range(5):
                    filename = 'file{}.txt'.format(i+1)
                    zip.writestr(filename, "{} {}'s data".format(fname, lname))

    def create_txtfile(path):
        with open(path, 'w') as out:
            out.write("Submission time: 12:00:00 June 3th 2017\n")
            out.write("Name: {} {}\n".format(fname, lname))
            out.write("Blah blah blah\n")
                    
    basename = 'testdata/submission-{}-2017-06-03-12-00-00'.format(id)
    
    create_zipfile(basename + '.zip')
    create_txtfile(basename + '.txt')
    

def main():
    if os.path.exists('testdata'):
        print('Test data already exists; delete it if you want to recreate test data')
    else:
        create_test_data()


if __name__ == '__main__':
    main()
