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
