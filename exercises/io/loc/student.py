import re
import os


def is_loc(line):
    """
    is_loc(line) geeft een truthy waarde terug indien
    de gegeven string line niet leeg is
    en niet uitsluitend commentaar bevat.
    Commentaar begint met een #.
    """
    raise NotImplementedError()


def loc_in_file(filename):
    """
    loc_in_file(filename) opent het bestand filename
    en telt het aantal regels code. Deze
    functie steunt op is_loc om te bepalen welke
    regels meetellen als code.
    """
    raise NotImplementedError()


def loc_in_directory(path):
    """
    loc_in_directory(path) telt het aantal lijnen code
    in de gegeven directory. Dit houdt in
    dat elk .py bestand moet bekeken worden
    en dat er recursief alle subdirectories
    worden afgegaan.
    """
    raise NotImplementedError()
