import re
from functools import reduce


def readMorse():
    def parse(line):
        return tuple(reversed(line.strip().split(' ')))
        
    with open('morse.txt', 'r') as lines:
        return dict([ parse(line) for line in lines ])


def decodeMorse(code):
    """
    Decodes the given code.
    """
    morse = readMorse()

    return "".join([ morse[token] for token in code.split(' ') if len(token) > 0 ])
