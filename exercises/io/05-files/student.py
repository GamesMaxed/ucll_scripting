from os import listdir
from os.path import isfile, join

def files(path):
    """
    Geeft een lijst van bestandsnamen terug in de gegeven directory.
    Enkel bestanden moeten opgelijst worden, geen directories.

    Zoek zelf op hoe je in Python een lijst van bestanden opvraagt
    en hoe je kan weten of het gaat om een bestand of een directory.
    """
    return [filename for filename in listdir(path) if isfile(join(path, filename))]


if __name__ == '__main__':
    """
    Indien er een command line argument werd meegeleverd,
    stelt dit het pad voor waarin naar bestanden moeten worden
    gezocht.
    Indien er geen command line argument gegeven werd,
    wordt er gekeken in de huidige directory.
    Je kan verwijzen naar de huidige directory met '.'.
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, default='.', help='Path to the directory')
    path = parser.parse_args().path
    print(*files(path), sep='\n')