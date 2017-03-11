import sys
import os


def contents(path):
    """
    Geeft de inhoud van het gegeven bestand
    terug als een lijst strings.
    De newlines op het einde van elke string
    moet verwijderd zijn geweest.
    Zoek op hoe je deze trailing newline
    het best verwijderd in Python.
    """
    with open(path, 'r') as file:
        return [ line.rstrip('\n') for line in file ]


# Print de inhoud af van alle bestanden
# waarvan de namen werd meegegeven als command
# line arguments.
if __name__ == '__main__':
    for file in sys.argv[1:]:
        for line in contents(file):
            print(line)
