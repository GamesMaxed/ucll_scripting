import re


def contains_twice(text, fragment):
    """
    Geeft truthy waarde indien text het fragment twee maal bevat,
    anders falsey waarde.

    Bijvoorbeeld, "abcxyzabc" bevat "abc" twee maal.
    """

    return bool(re.search(fragment + '.*' + fragment, text))
