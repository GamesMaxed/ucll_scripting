def count_common_chars(s1, s2):
    """
    Given two strings s1 and s2, counts
    the number of characters they have in common,
    i.e. these characters must be equal and
    appear at the same location in the strings.

    For example, 'abcd' and 'a123' have one character in common.
                 'ab' and 'ba' have 0 characters in common.
    """
    raise NotImplementedError()


def hack(candidates, attempt):
    """
    Hacks the system.

    candidates is a list of strings representing potential passwords.
    attempt is a function that takes one argument X and returns
    the number of characters the argument X and the actual password
    have in common. This function can only be called a finite number of times.

    hack should return the correct password, i.e. one of the
    strings in the list candidates for which attempt
    returned a value indicating that all characters were correct.
    """
    raise NotImplementedError()
