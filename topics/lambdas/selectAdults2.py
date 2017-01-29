def select_adults(persons):
    result = []

    for person in persons:
        if `\pgfmark{select_adults start}`person.age >= 18`\pgfmark{select_adults end}`:
            result.append(person)

    return result

# Verderop
adults = select_adults(persons)
