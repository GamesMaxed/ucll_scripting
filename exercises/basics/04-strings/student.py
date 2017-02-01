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
