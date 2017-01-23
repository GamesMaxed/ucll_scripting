import re


def findRepetition(string):
    """
    Returns a substring of at least 4 characters
    that is repeated in the given string.
    If multiple such substrings exist, the leftmost
    is returned.

    For example, "abcd,abcd" contains "abcd" twice.
    """

    match = re.search(r'(.{4,}).*\1', string)
    
    if match:
        return match.group(1)
    else:
        return None
