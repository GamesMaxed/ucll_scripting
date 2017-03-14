import urllib.request
import zipfile
import os


def download_package():
    if os.path.isfile('imdb.zip'):
        print('Already downloaded imdb.zip')
    else:    
        print('Downloading imdb.zip')
        urllib.request.urlretrieve('http://alexander.khleuven.be/courses/scripting/extra/imdb.zip', 'imdb.zip')

        print('Unpacking imdb.zip')
        with zipfile.ZipFile('imdb.zip', 'r') as zip:
            zip.extractall()
        

if __name__ == '__main__':
    download_package()
