import re
from functools import reduce


def readMorseToPlaintextDictionary():
    with open('morse.txt', 'r') as lines:
        return dict([ tuple(reversed(line.strip().split(' '))) for line in lines ])

def readPlaintextToMorseDictionary():
    with open('morse.txt', 'r') as lines:
        return dict([ tuple(line.strip().split(' ')) for line in lines ])

def decodeMorse(code):
    """
    Decodes the given code to plaintext.
    """
    morse = readMorseToPlaintextDictionary()

    return "".join([ morse[token] for token in code.split(' ') if len(token) > 0 ])


def encodeMorse(plaintext):
    """
    Translates given plaintext to morse.
    """
    morse = readPlaintextToMorseDictionary()
    
    return " ".join([ morse[char] for char in plaintext ])
