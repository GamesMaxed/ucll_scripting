def get_ages(persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{get_ages2 start}`p.age`\pgfmark{get_ages2 end}`)

    return result
