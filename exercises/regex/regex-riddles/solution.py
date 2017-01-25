import re

def riddle1(string):
    # Exactly 3 characters long
    return re.fullmatch(r'...', string)

def riddle2(string):
    return re.fullmatch(r'a*b*', string)

def riddle3(string):
    return re.fullmatch(r'(a|b)*', string)

def riddle4(string):
    return re.search(r'a.*a.*a.*a', string)

def riddle5(string):
    return re.fullmatch(r'(\d)\1\1', string)

def riddle6(string):
    return re.fullmatch(r'(\d+)\1\1', string)

def riddle7(string):
    return re.fullmatch(r'\D*', string)

def riddle8(string):
    return re.fullmatch(r'a?b?c?', string)

def riddle9(string):
    return re.fullmatch(r'(.)(.)(\1\2)*\1', string)
