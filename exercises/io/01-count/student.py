def count_lines(stream):
    """
    Telt het aantal regels in het bestand.
    Nota: het argument stream is een reeds
    geopend bestand. Je hoeft hier dus
    niet open op te roepen.
    """

    raise NotImplementedError()


def count_words(stream):
    """
    Telt het aantal woorden in de input stream.
    Woorden zijn tekenreeksen die gescheiden worden
    door whitespace.
    """

    raise NotImplementedError()
    

def count_chars(stream):
    """
    Telt het aantal tekens in de input stream.
    """

    raise NotImplementedError()


def main():
    """
    Bekijkt command line arguments en roept
    de juiste functie op met de juiste stream.

    Syntax:
        python student.py option filename
    waarbij
    * option: een van lines, words, of chars
    * filename: bestandsnaam of - voor stdin

    Bv.
        python student.py lines file.txt
    telt het aantal lijnen in bestand file.txt
        python student.py words -
    telt het aantal woorden uit stdin
    """


# Checkt of dit python bestand rechtstreeks wordt
# opgeroepen of wordt ingeladen als library
if __name__ == '__main__':
    # Voer main() uit indien dit script
    # rechtstreeks uitgevoerd wordt
    main()
    
