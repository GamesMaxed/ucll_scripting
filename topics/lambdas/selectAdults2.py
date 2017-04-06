def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults2 start}`person.age >= 18`\pgfmark{selectAdults2 end}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
