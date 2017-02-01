def is_binary(string):
    for c in string:
        if c != '0' and c != '1':
            return False

    return True

def to_binary(n):
    if n < 0:
        raise RuntimeError("n must be positive")
    elif n == 0:
        return "0"
    else:
        result = ""

        while n > 0:
            result = str(n % 2) + result
            n = n // 2

        return result

def from_binary(string):
    result = 0

    for char in string:
        if char == '0':
            digit = 0
        elif char == '1':
            digit = 1
        else:
            raise RuntimeError('Invalid digit')
        
        result = result * 2 + digit

    return result

def has_extension(filename, extension):
    extension = '.' + extension

    if len(filename) < len(extension):
        return False
    else:
        return filename[-len(extension):] == extension

def format_date(day, month, year):
    return "{}/{}/{}".format(day, month, year)

def format_time(hours, minutes, seconds, milliseconds):
    return "{}:{}:{}.{}".format(hours, minutes, seconds, milliseconds)
