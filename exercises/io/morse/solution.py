import re
from functools import reduce


def read_morse_to_plaintext_dictionary():
    with open('morse.txt', 'r') as lines:
        return dict([ tuple(reversed(line.strip().split(' '))) for line in lines ])

def read_plaintext_to_morse_dictionary():
    with open('morse.txt', 'r') as lines:
        return dict([ tuple(line.strip().split(' ')) for line in lines ])

def decode_morse(code):
    """
    Decodes the given code to plaintext.
    """
    morse = read_morse_to_plaintext_dictionary()

    return "".join([ morse[token] for token in code.split(' ') if len(token) > 0 ])


def encode_morse(plaintext):
    """
    Translates given plaintext to morse.
    """
    morse = read_plaintext_to_morse_dictionary()
    
    return " ".join([ morse[char] for char in plaintext ])
