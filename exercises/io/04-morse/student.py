def decode_morse(code: str):
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
    dictionary = {}
    with open('morse.txt', 'r') as file:
        for line in file:
            letter, morsecode = line.split(' ')
            dictionary[morsecode.rstrip('\n')] = letter

    return "".join([dictionary[token] for token in code.split(' ') if len(token) > 0])


def encode_morse(plaintext):
    """
    Zet de gegeven string om naar plaintext.
    De string bestaat uitsluitend uit
    tekens die ook voortkomen in morse.txt,
    m.a.w. er komen geen spaties in voor.
    """
    dictionary = {}
    with open('morse.txt', 'r') as file:
        for line in file:
            letter, morsecode = line.split(' ')
            dictionary[letter] = morsecode.rstrip('\n')

    return " ".join([dictionary[letter] for letter in plaintext])