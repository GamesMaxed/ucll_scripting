import re


def compress(string):
    """
    Run Length Encoding is een eenvoudige compressievorm
    waarbij men een reeks van N keer hetzelfde teken X 
    vervangt door NX. Bijvoorbeeld, "aaaa" vervangt men door "4a".

    compress(string) moet elke reeks letters vervangen
    door de RLE ervan. Andere tekens blijven onveranderd. Enkele voorbeelden:

    "a"          -> "1a"
    "aaaaa"      -> "5a"
    "aaBBB"      -> "2a3B"
    "a, b, c"    -> "1a, 1b, 1c"
    """

    raise NotImplementedError()


def decompress(string):
    """
    Decompress is de inverse operatie van compress:
    in de gegeven string wordt elk patroon 'NX'
    met N een getal en X een letter omgezet
    naar N X'en na elkaar. Bijvoorbeeld,
    "3a" wordt "aaa".
    """

    raise NotImplementedError()


# Het script ontvangt de te verwerken data
# via stdin en voert het uit via stdout.
# Een command line argument geeft
# aan of er moet gecomprimeerd of
# gedecomprimeerd moet worden:
#    cat plaintext.txt | python student.py compress
# of
#    cat compressed.txt | python student.py decompress
if __name__ == '__main__':
    raise NotImplementedError()
