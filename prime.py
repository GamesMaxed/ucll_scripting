def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1

def nth_prime(n):
    k = 0

    while n > 0:
        k += 1
        
        if is_prime(k):
            n -= 1

        

    return k



for i in range(1, 100):
    print( nth_prime(i) )
