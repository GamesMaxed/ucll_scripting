def is_adult(person):
    return `\pgfmark{selectAdults3 age start}`person.age >= 18`\pgfmark{selectAdults3 age end}`

def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults3 isadult start}`is_adult(person)`\pgfmark{selectAdults3 isadult end}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
