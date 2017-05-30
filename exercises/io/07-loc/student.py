import sys
import re
import os
import pathlib


languages = {
    '.py': '#',
    '.rb': '#',
    '.java': '//',
    '.cpp': '//',
    '.hs': '--',
    '.tex': '%',
    '.cl': '%'
}

def is_loc(line: str, comment_delimiter: str):
    """
    Gaat na of de string line meetelt als line of code (loc).
    Dit is het geval indien de string een niet-whitespace
    teken bevat dat niet in commentaar staat.
    Commentaar begint met de gegeven comment_delimiter.
    Voor Python is dit #, voor Java is dit //, etc.

    Voorbeelden:
      is_loc('aaa', '#') geeft True
      is_loc('      ', '#') geeft False omdat de string enkel whitespace bevat
      is_loc('     x', '//') geeft True
      is_loc('    // klk', '//') geeft False omdat er buiten de commentaar enkel whitespace is
    """
    line = line.strip()
    return len(line) > 0 and not line.startswith(comment_delimiter)


def extension_of(filename: str):
    """
    Geeft de extensie terug van het bestand.
    Het punt moet mee in het resultaat zitten.
    Bv. extension_of('bla.txt') geeft '.txt' als resultaat.

    Deze functionaliteit is reeds geimplementeerd
    in een Python library. Zoek op waar (bv. google naar 'python get file extension')
    en maak er gebruik van.
    """
    return pathlib.Path(filename).suffix
    

def is_source_file(filename):
    """
    Gaat na of het gegeven bestand source code bevat,
    afgaande op de extensie. Zie readme.txt.
    """
    return extension_of(filename) in languages.keys()


def comment_delimiter_for(filename):
    """
    Geeft de comment delimiter terug voor de gegeven bestandsnaam.
    Zie readme.txt.

    Bijvoorbeeld,
      comment_delimiter_for('foo.py') geeft '#'
      comment_delimiter_for('foo.java') geeft '//'
    """
    return languages[extension_of(filename)]


def loc(source: str, delimiter: str):
    """
    Telt het aantal loc in de string source, ervan uitgaande
    dat commentaar begint met de gegeven delimiter.
    """
    return len([line for line in source.split('\n') if is_loc(line, delimiter)])


def loc_in_file(filename):
    """
    Telt het aantal loc in het gegeven bestand.
    Indien het bestand geen source code bevat
    (zie is_source_file), dan geeft deze functie 0 terug.
    """
    if not is_source_file(filename):
        return 0

    with open(filename) as file:
        return loc("".join(file.readlines()), languages[extension_of(filename)])


def loc_in_directory(path):
    """
    Telt het aantal loc in de gegeven directory.
    Deze functie gaat op zoek naar alle source files
    in de gegeven directory en zoekt tevens recursief
    in alle subdirectories.
    Enkel source files komen in aanmerking.
    """
    return sum(loc_in_directory(entry) if entry.is_dir() else loc_in_file(entry) for entry in os.scandir(path))


if __name__ == '__main__':
    """
    Het command line argument geeft het pad van de directory
    aan waarin alle locs worden geteld.
    Indien er geen command line argument geleverd werd,
    wordt geteld in de huidige directory.
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, default='.', help='Path to the directory')
    path = parser.parse_args().path
    print(loc_in_directory(path))
