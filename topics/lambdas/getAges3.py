def get_age(person):
    return `\pgfmark{get_ages3 start1}`person.age`\pgfmark{get_ages3 end1}`

def get_ages(persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{get_ages3 start2}`get_age(p)`\pgfmark{get_ages3 end2}`)

    return result
