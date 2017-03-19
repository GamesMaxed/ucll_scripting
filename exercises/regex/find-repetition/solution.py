import re


def find_repetition(string):
    """
    Zoekt naar een deelstring van minstens 4 tekens
    lang die herhaald wordt in de gegeven string.

    Bijvoorbeeld, "abcdxxxabcd" bevat "abcd" dubbel.

    Indien er meerdere herhaalde deelstrings bestaan,
    wordt de meest linkse teruggegeven.
    """

    match = re.search(r'(.{4,}).*\1', string)
    
    if match:
        return match.group(1)
    else:
        return None
