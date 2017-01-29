def get_ages(persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{getAges2 start}`p.age`\pgfmark{getAges2 end}`)

    return result
