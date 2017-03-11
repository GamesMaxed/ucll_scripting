import sys


def diff(path1, path2):
    """
    Vergelijkt de overeenkomstige regels uit beide bestanden
    (de eerste regel uit bestand file1 met de eerste regel uit bestand file2, etc.)
    en geeft een lijst terug van verschillende regels.
    Deze lijst bestaat uit triplets (index, regel1, regel2) waarbij
     * index de regelindex aangeeft (tellend vanaf 0),
     * regel1 de regel uit file1,
     * regel2 de regel uit file2.
    """
    with open(path1, 'r') as file1, open(path2, 'r') as file2:
        return [ (index, line1, line2) for index, line1, line2 in zip(range(0, 2**32), file1, file2) if line1 != line2 ]


if __name__ == '__main__':
    for (index, line1, line2) in diff(sys.argv[1], sys.argv[2]):
        print("Line {}\n{}{}".format(index + 1, line1, line2))
