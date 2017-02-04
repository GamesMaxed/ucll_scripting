def create_interval(a, b):
    result = set()

    for i in range(a, b + 1):
        result.add(i)

    return result

# Kortere implementatie
def create_interval(a, b):
    return set( range(a, b+1) )


