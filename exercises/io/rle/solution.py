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
    def aux(match):
        return "{}{}".format(len(match.group(0)), match.group(1))
        
    return re.sub(r'([a-zA-Z])\1*', aux, string)


def decompress(string):
    """
    Decompress is de inverse operatie van compress:
    in de gegeven string wordt elk patroon 'NX'
    met N een getal en X een letter omgezet
    naar N X'en na elkaar. Bijvoorbeeld,
    "3a" wordt "aaa".
    """

    def aux(match):
        return match.group(2) * int(match.group(1))

    return re.sub(r'(\d+)(\w)', aux, string)

