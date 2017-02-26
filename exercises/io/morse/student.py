import re
from functools import reduce



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

    raise NotImplementedError()


def encode_morse(plaintext):
    """
    Zet de gegeven string om naar plaintext.
    De string bestaat uitsluitend uit
    tekens die ook voortkomen in morse.txt,
    m.a.w. er komen geen spaties in voor.
    """

    raise NotImplementedError()
    

