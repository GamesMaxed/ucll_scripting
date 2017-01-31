import urllib.request
import zipfile
import os


def download_dictionary():
    if os.path.isfile('dictionary.txt'):
        print('skipping dictionary.txt')
    else:    
        print('Downloading dictionary.zip')
        urllib.request.urlretrieve('http://alexander.khleuven.be/courses/scripting/extra/dictionary.zip', 'dictionary.zip')

        print('Unpacking dictionary.zip')
        with zipfile.ZipFile('dictionary.zip', 'r') as zip:
            zip.extractall()

        print('Deleting dictionary.zip')
        os.remove('dictionary.zip')




if __name__ == '__main__':
    download_dictionary()
