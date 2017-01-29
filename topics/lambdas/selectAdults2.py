def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults start}`person.age >= 18`\pgfmark{selectAdults end}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
