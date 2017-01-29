def get_height(person):
    return person.height

ages = map(persons, get_height)

# kan geschreven worden als

map(persons, lambda p: p.height)
