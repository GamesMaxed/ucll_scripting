def isOdd(x):
    return x % 2 == 1

# any gaat na of er een element
# is waarvoor de functie een
# truthy waarde teruggeeft
any(isOdd, [1,2,3,4,5])   # True
any(isOdd, [2,4,6,8])     # False
