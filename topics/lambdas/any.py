def is_odd(x):
    return x % 2 == 1

# any gaat na of er een element
# is waarvoor de functie een
# truthy waarde teruggeeft
any(is_odd, [1,2,3,4,5])   # True
any(is_odd, [2,4,6,8])     # False
