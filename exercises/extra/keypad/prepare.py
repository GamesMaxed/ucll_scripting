import urllib.request
import zipfile
import os


def download_package():
    if os.path.isfile('words.zip'):
        print('Already downloaded words.zip')
    else:    
        print('Downloading wrods.zip')
        urllib.request.urlretrieve('http://alexander.khleuven.be/courses/scripting/extra/words.zip', 'words.zip')

        print('Unpacking words.zip')
        with zipfile.ZipFile('words.zip', 'r') as zip:
            zip.extractall()
        

if __name__ == '__main__':
    download_package()

