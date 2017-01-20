def selectAdults(persons):
    result = []

    for person in persons:
        if person.age >= 18:
            result.append(person)

    return result
