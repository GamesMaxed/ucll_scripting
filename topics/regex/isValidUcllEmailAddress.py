def isValidUcllEmailAddress(str):
    regex = r"\w+\.\w+@(student\.)?ucll\.be"
    return re.fullmatch(regex, str)
