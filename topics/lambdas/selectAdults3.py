def is_adult(person):
    return `\pgfmark{selectAdults3 start}`person.age >= 18`\pgfmark{selectAdults3 end}`

def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults3b start}`is_adult(person)`\pgfmark{selectAdults3b end}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
