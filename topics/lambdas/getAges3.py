def getAge(person):
    return `\pgfmark{getAges3 start1}`person.age`\pgfmark{getAges3 end1}`

def getAges(persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{getAges3 start2}`getAge(p)`\pgfmark{getAges3 end2}`)

    return result
