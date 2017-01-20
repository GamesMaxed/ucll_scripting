def getHeight(person):
    return person.height

ages = map(persons, getHeight)

# kan geschreven worden als

map(persons, lambda p: p.height)
