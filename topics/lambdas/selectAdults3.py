def is_adult(person):
    return `\pgfmark{selectAdults2 start1}`person.age >= 18`\pgfmark{selectAdults2 end1}`

def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults2 start2}`is_adult(person)`\pgfmark{selectAdults2 end2}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
