import re


def containsTwice(text, fragment):
    """
    Returns True if text contains fragment twice.

    For example, "abcxyzabc" contains "abc" twice.
    """

    return bool(re.search(fragment + '.*' + fragment, text))
