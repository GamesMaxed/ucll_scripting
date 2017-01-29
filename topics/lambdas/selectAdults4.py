def is_adult(person):
    return person.age >= 18

def filter(`\pgfmark{select_adults3 start1}`condition`\pgfmark{select_adults3 end1}`, persons):
    result = []

    for person in persons:
        if `\pgfmark{select_adults3 start2}`condition(person)`\pgfmark{select_adults3 end2}`:
            result.append(person)

    return result

# Verderop
adults = filter(`\pgfmark{select_adults3 start3}`is_adult`\pgfmark{select_adults3 end3}`, persons)
