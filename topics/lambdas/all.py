def is_odd(x):
    return x % 2 == 1

# all gaat na of de functie
# voor alle elementen
# een truthy waarde teruggeeft
all(is_odd, [1,2,3,4,5])   # False
all(is_odd, [1,3,5,7])     # True
