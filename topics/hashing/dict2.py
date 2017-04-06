def ord(letter):
    if letter == 'a': return 0
    # ...

def ord2(letter1, letter2):
    return ord(letter1) * 26 + ord(letter2)

def lookup(pages, name):
    first_letter = name[0]
    second_letter = name[1]
    index = ord2(first_letter, second_letter)
    page = pages[index]
    return page.find(name)
