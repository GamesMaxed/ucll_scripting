def select_persons(persons,
                  minAge = None, \
                  maxAge = None, \
                  name = None, \
                  minWeight = None, \
                  maxWeight = None, \
                  minHeight = None, \
                  maxHeight = None, \
                  minBMI = None, \
                  maxBMI = None):
    result = []

    for p in persons:
        if (minAge == None or minAge <= p.age) and \
           (maxAge == None or p.age <= maxAge) and \
           (name == None or p.name == name) and \
           (minWeight == None or minWeight <= p.weight) and \
           ...
        result.append(p)

    return result
