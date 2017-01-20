def selectAdults(persons):
    result = []

    for person in persons:
        if person.age >= 100:
            result.append(person)

    return result
