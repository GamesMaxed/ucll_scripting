import re


def isValidPassword(password):
    """
    Returns a truthy value if the given password is valid,
    a falsey value otherwise.

    A password is valid if it is at least
    8 characters long, contains a lowercase letter,
    an uppercase letter, a digit and
    a special character.
    Special characters are !?.()-*+
    """

    return all(re.search(regex, password) for regex in [ r'.{8,}', r'[a-z]', r'[A-Z]', r'\d', r'[!?.()-*+]' ])
