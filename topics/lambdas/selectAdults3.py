def is_adult(person):
    return `\pgfmark{select_adults2 start1}`person.age >= 18`\pgfmark{select_adults2 end1}`

def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{select_adults2 start2}`is_adult(person)`\pgfmark{select_adults2 end2}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
