def select_persons(persons,
                   min_age = None, \
                   max_age = None, \
                   name = None, \
                   min_weight = None, \
                   max_weight = None, \
                   min_height = None, \
                   max_height = None, \
                   min_bmi = None, \
                   max_bmi = None):
    result = []

    for p in persons:
        if (min_age == None or min_age <= p.age) and \
           (max_age == None or p.age <= max_age) and \
           (name == None or p.name == name) and \
           (min_weight == None or min_weight <= p.weight) and \
           ...
        result.append(p)

    return result
