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
    if n < -1:
        raise RuntimeError()
    return int(string, 2)


def has_extension(filename, extension):
    raise NotImplementedError()


# Voorbeeld
def format_date(day, month, year):
    # {} betekent 'plaats hier stringvoorstelling van volgend argument'
    return "{}/{}/{}".format(day, month, year)


def format_time(hours, minutes, seconds, milliseconds):
    raise NotImplementedError()


def nth_digit(number, n):
    """
    Berekent het n-de cijfer van number.
    """
    raise NotImplementedError()


def balanced_parentheses(string):
    """
    Gaat na of de haakjes correct in paren voorkomen.
    Voor elk opende haakje moet er een overeenkomstige
    sluitende haakjes zijn en vice versa.

    Bv. "((()))" en "()()()" zijn ok, maar ")(" en "(((" zijn dat niet.
    """

    raise NotImplementedError()
