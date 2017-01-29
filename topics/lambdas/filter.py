def is_odd(x):
    return x % 2 == 1

# filter selecteert alle elementen
# waarvoor de gegeven functie
# een truthy waarde teruggeeft
ns = filter(is_odd, [1,2,3,4,5])

# ns == [1,3,5]
