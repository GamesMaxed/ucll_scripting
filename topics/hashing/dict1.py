def ord(letter):
    if letter == 'a': return 0
    elif letter == 'b': return 1
    # ...

# pages: list van pagina's
def lookup(pages, name):
    first_letter = name[0]
    index = ord(first_letter)
    page = pages[index]
    return page.find(name)
