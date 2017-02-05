def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


def count_primes_below(n):
    raise NotImplementedError()


def gcd(x, y):
    raise NotImplementedError()


# Rekent de som van de cijfers van n op
def sum_digits(n):
    raise NotImplementedError()
