import sys
import os


def files(path):
    """
    Geeft een lijst van bestandsnamen terug in de gegeven directory.
    Enkel bestanden moeten opgelijst worden, geen directories.

    Zoek zelf op hoe je in Python een lijst van bestanden opvraagt
    en hoe je kan weten of het gaat om een bestand of een directory.
    """
    return [ file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) ]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[2]
    else:
        path = '.'

    for file in files(path):
        print(file)
