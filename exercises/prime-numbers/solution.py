def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


def nthPrime(n):
    k = 0

    while n > 0:
        k += 1
        if isPrime(k):
            n -= 1

    return k


def primesUpTo(n):
    return [ k for k in range(1, n+1) if isPrime(k) ]

def factorInteger(n):
    primes = primesUpTo(n)
    primeIndex = 0
    result = []

    while n != 1:
        currentPrime = primes[primeIndex]
        
        if n % currentPrime == 0:
            result.append(currentPrime)
            n /= currentPrime
        else:
            primeIndex += 1

    return result
