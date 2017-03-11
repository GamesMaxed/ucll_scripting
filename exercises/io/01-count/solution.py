import sys


def count_lines(stream):
    """
    Telt het aantal regels in de input stream.
    """
    return len(stream.readlines())


def count_words(stream):
    """
    Telt het aantal woorden in de input stream.
    Woorden zijn tekenreeksen die gescheiden worden
    door whitespace.
    """
    return sum( len(line.split()) for line in stream )


def count_chars(stream):
    """
    Telt het aantal tekens in de input stream.
    """
    return sum( len(line) for line in stream )


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Two arguments required')
    else:
        option = sys.argv[1]
        file = sys.argv[2]
    
        if option == 'lines':
            func = count_lines
        elif option == 'words':
            func = count_words
        elif option == 'chars':
            func = count_chars
        else:
            sys.stderr.write('Unknown option {}\n'.format(option))

        if file == '-':
            print(func(sys.stdin))
        else:
            with open(file, 'r') as input:
                print(func(input))


if __name__ == '__main__':
    main()
    
