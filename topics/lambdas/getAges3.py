def get_age(person):
    return `\pgfmark{getAges3 start1}`person.age`\pgfmark{getAges3 end1}`

def get_ages(persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{getAges3 start2}`get_age(p)`\pgfmark{getAges3 end2}`)

    return result
