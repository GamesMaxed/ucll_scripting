def isAdult(person):
    return `\pgfmark{selectAdults2 start1}`person.age >= 18`\pgfmark{selectAdults2 end1}`

def selectAdults(persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults2 start2}`isAdult(person)`\pgfmark{selectAdults2 end2}`:
            result.append(person)

    return result

# Verderop
adults = selectAdults(persons)
