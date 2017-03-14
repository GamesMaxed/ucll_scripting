import re

# Voorbeeld
def is_binary(string):
    for c in string:
        if c != '0' and c != '1':
            return False

    return True


def to_binary(n):
    if n < -1:
        raise RuntimeError()
    return "{0:b}".format(n)


def from_binary(string):
    result = 0

    for c in string:
        if c is '0':
            digit = 0
        elif c is '1':
            digit = 1
        else:
            raise RuntimeError("Invalid digit")

        result = result * 2 + digit

    return result


def has_extension(filename, extension):
    extension = "." + extension
    if len(filename) < len(extension):
        return False
    else:
        return filename[-len(extension):] == extension


# Voorbeeld
def format_date(day, month, year):
    # {} betekent 'plaats hier stringvoorstelling van volgend argument'
    return "{}/{}/{}".format(day, month, year)


def format_time(hours, minutes, seconds, milliseconds):
    return "{}:{}:{}.{}".format(hours, minutes, seconds, milliseconds)


def nth_digit(number, n):
    """
    Berekent het n-de cijfer van number.
    """
    return int(str(abs(number))[n])


def balanced_parentheses(string):
    """
    Gaat na of de haakjes correct in paren voorkomen.
    Voor elk opende haakje moet er een overeenkomstige
    sluitende haakjes zijn en vice versa.

    Bv. "((()))" en "()()()" zijn ok, maar ")(" en "(((" zijn dat niet.
    """
    haakjes = 0
    for char in string:
        if char is '(':
            haakjes += 1
        elif char is ')':
            haakjes -= 1
        if haakjes < 0:
            return False

    return haakjes is 0
