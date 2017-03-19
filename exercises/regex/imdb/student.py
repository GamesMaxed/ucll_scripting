import re

'''
Voer eerst "prepare" uit in de shell in deze directory
Dit downloadt de nodige bestanden voor deze opgave

Voor deze opgave moet je de nodige informatie
ophalen uit het bestand ratings.txt.
'''

def find_episode_titles(series):
    """
    Gegeven de naam van een serie (bv. "Rick and Morty")
    geeft deze functie een lijst terug van de namen
    van de afleveringen ("Pilot", "Lawnmower Dog", "Anatomy Park", ...)
    terug. 

    De lijst moet chronologisch gesorteerd zijn.
    Zoek hiervoor op hoe 'sorted' werkt in Python.
    """
    raise NotImplementedError()
    

def best_movie_from_year(year, minimum_count = 10000):
    """
    Zoekt naar de hoogst scorende film uit het opgegeven jaar.
    Enkel films die meer dan minimum_count ratings hebben
    ontvangen komen in aanmerking.
    """
    raise NotImplementedError()


def series_average_ratings():
    """
    Geeft een lijst koppels (serie, gemiddelde_score) terug,
    gesorteerd van groot naar klein. Enkel series
    komen in aanmerking, en de gemiddelde score
    wordt berekend op basis van de scores van de
    individuele afleveringen.
    """
    raise NotImplementedError()
