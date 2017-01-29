def get_age(person):
    return person.age

ages = map(persons, get_age)

# kan geschreven worden als

map(persons, lambda p: p.age)
