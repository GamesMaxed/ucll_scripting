def select_adults(persons):
    result = []

    for person in persons:
        if person.age >= 18:
            result.append(person)

    return result
