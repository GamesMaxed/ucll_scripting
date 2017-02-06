def corresponding_letters(n):
    xs = [ None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz' ]
    return set(xs[n])


def read_words():
    with open('words.txt', 'r') as file:
        return [ line.strip() for line in file ]

def find_words(words, digits):
    words = [ word for word in words if len(word) == len(digits) ]

    for index in range(0, len(digits)):
        letters = corresponding_letters(digits[index])
        words = [ word for word in words if word[index] in letters ]

    return words


if __name__ == '__main__':
    digits = [ int(char) for char in sys.argv[1] ]
    words = read_words()

    for word in find_words(words, digits):
        print(word)
    
