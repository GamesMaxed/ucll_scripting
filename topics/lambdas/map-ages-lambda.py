def getAge(person):
    return person.age

ages = map(persons, getAge)

# kan geschreven worden als

map(persons, lambda p: p.age)
