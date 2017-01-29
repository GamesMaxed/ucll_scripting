def select_older_than(persons, age):
    result = []

    for person in persons:
        if person.age >= age:
            result.append(person)

    return result
