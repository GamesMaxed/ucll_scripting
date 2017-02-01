# Voorbeeld
def is_binary(string):
    for c in string:
        if c != '0' and c != '1':
            return False

    return True


def to_binary(n):
    raise NotImplementedError()


def from_binary(string):
    raise NotImplementedError()


def has_extension(filename, extension):
    raise NotImplementedError()


# Voorbeeld
def format_date(day, month, year):
    # {} betekent 'plaats hier stringvoorstelling van volgend argument'
    return "{}/{}/{}".format(day, month, year)


def format_time(hours, minutes, seconds, milliseconds):
    raise NotImplementedError()
