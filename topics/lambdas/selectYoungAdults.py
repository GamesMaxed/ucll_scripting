def select_young_adults(persons):
    result = []

    for p in persons:
        if 18 <= p.age and p.age <= 25:
            result.append(p)

    return result
