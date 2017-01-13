def scramble(str):
    def scramble(word):
        letters = list(word)
        shuffle(letters)
        return "".join(letters)

    return re.sub(r'([a-z])([a-z]+)([a-z])',
                  lambda match: match.group(1) +
                                scramble(match.group(2)) +
                                match.group(3), str)
