def diff(file1, file2):
    """
    Vergelijkt de overeenkomstige regels uit beide bestanden
    (de eerste regel uit bestand file1 met de eerste regel uit bestand file2, etc.)
    en geeft een lijst terug van verschillende regels.
    Deze lijst bestaat uit triplets (index, regel1, regel2) waarbij
     * index de regelindex aangeeft (tellend vanaf 0),
     * regel1 de regel uit file1,
     * regel2 de regel uit file2.
    """
    raise NotImplementedException()



# Indien deze code opgeroepen wordt via de command line
# moeten de te vergelijken bestanden als command line arguments
# meegeleverd worden:
#   python student.py file1 file2
# Per regel die verschilt wordt afgedrukt:
#   Line <index>
#   <Regel uit bestand file1>
#   <Regel uit bestand file2>
#   <lege lijn>
# Index moet beginnen tellen bij 1.
if __name__ == '__main__':
    raise NotImplementedException
