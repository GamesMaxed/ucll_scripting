# Voorbeeld
def abs(x):
    if x < 0:
        return -x
    else:
        return x

# Merk op dat 'else if' in Python een speciale syntax heeft
# Zoek deze zelf op online
def sign(x):
    if x < 0: return -1
    if x is 0: return 0
    return 1

def factorial(n):
    if n in (0,1):
        return 1
    return n * factorial(n-1)
