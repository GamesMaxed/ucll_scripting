import sys


def read_morse_to_plaintext_dictionary():
    with open('morse.txt', 'r') as lines:
        return dict([ tuple(reversed(line.strip().split(' '))) for line in lines ])

def read_plaintext_to_morse_dictionary():
    with open('morse.txt', 'r') as lines:
        return dict([ tuple(line.strip().split(' ')) for line in lines ])

def decode_morse(code):
    """
    Decodeert de gegeven morsecode.
    De morsecode bestaan uit '.' en '-'
    en de groepjes tekens die overeenkomen
    met een enkele letter of getal
    worden gescheiden door een spatie.
    Bv. '... --- ...' voor SOS (en niet '...---...')

    Steunt op het bestand morse.txt om
    de morsecodes in te lezen.
    """
    morse = read_morse_to_plaintext_dictionary()

    return "".join([ morse[token] for token in code.split(' ') if len(token) > 0 ])


def encode_morse(plaintext):
    """
    Zet de gegeven string om naar plaintext.
    De string bestaat uitsluitend uit
    tekens die ook voortkomen in morse.txt,
    m.a.w. er komen geen spaties in voor.
    """
    morse = read_plaintext_to_morse_dictionary()
    
    return " ".join([ morse[char] for char in plaintext ])
