def count_lines(stream):
    """
    Telt het aantal regels in het bestand.
    Nota: het argument stream is een reeds
    geopend bestand. Je hoeft hier dus
    niet open op te roepen.
    """
    return len(stream.readlines())


def count_words(stream):
    """
    Telt het aantal woorden in de input stream.
    Woorden zijn tekenreeksen die gescheiden worden
    door whitespace.
    """
    return sum(len(line.split()) for line in stream)


def count_chars(stream):
    """
    Telt het aantal tekens in de input stream.
    """
    return sum(len(line) for line in stream)


if __name__ == '__main__':
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
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('option', type=str, help='What to count')
    parser.add_argument('filename', type=str, help='File to be handled')
    args = parser.parse_args()

    with open(args.filename, 'r') as file:
        if args.option == 'lines':
            print(count_lines(file))
        if args.option == 'words':
            print(count_words(file))
        if args.option == 'chars':
            print(count_chars(file))