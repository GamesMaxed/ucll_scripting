def select_young_adults(persons):
    result = []

    for p in select_older_than(persons, 18):
        if p.age <= 25:
            result.append(p)

    return result
