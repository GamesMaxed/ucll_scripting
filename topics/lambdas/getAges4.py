def getAge(person):
    return person.age

def map(`\pgfmark{getAges4 start1}`function`\pgfmark{getAges4 end1}`, persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{getAges4 start2}`function(p)`\pgfmark{getAges4 end2}`)

    return result

ages = map(`\pgfmark{getAges4 start3}`getAge`\pgfmark{getAges4 end3}`, persons)
