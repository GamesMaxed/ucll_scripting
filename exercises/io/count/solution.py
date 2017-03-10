def count_lines(filename):
    """
    Telt het aantal regels in het bestand.
    """
    with open(filename, 'r') as file:
        return len(file.readlines())
