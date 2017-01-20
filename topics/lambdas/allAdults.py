def allAdults(persons):
    for p in persons:
        if not p.age >= 18:
            return False

    return True
