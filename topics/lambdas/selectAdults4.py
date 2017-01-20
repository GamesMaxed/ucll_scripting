def isAdult(person):
    return person.age >= 18

def filter(`\pgfmark{selectAdults3 start1}`condition`\pgfmark{selectAdults3 end1}`, persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults3 start2}`condition(person)`\pgfmark{selectAdults3 end2}`:
            result.append(person)

    return result

# Verderop
adults = filter(`\pgfmark{selectAdults3 start3}`isAdult`\pgfmark{selectAdults3 end3}`, persons)
