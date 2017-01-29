def get_age(person):
    return person.age

def map(`\pgfmark{get_ages4 start1}`function`\pgfmark{get_ages4 end1}`, persons):
    result = []

    for p in persons:
        result.append(`\pgfmark{get_ages4 start2}`function(p)`\pgfmark{get_ages4 end2}`)

    return result

ages = map(`\pgfmark{get_ages4 start3}`get_age`\pgfmark{get_ages4 end3}`, persons)
