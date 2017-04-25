def is_adult(person):
    return person.age >= 18

def filter(`\pgfmark{selectAdults4 start}`condition`\pgfmark{selectAdults4 end}`, persons):
    result = []

    for person in persons:
        if `\pgfmark{selectAdults4b start}`condition(person)`\pgfmark{selectAdults4b end}`:
            result.append(person)

    return result

# Verderop
adults = filter(`\pgfmark{selectAdults4c start}`is_adult`\pgfmark{selectAdults4c end}`, persons)
