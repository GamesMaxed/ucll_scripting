def count_adults(persons):
    result = 0

    for p in persons:
        if p.age >= 18:
            result += 1

    return result
