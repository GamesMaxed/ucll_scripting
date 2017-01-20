def selectYoungAdults(persons):
    result = []

    for p in selectOlderThan(persons, 18):
        if p.age <= 25:
            result.append(p)

    return result
