def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


def count_primes_below(n):
    raise NotImplementedError()


def gcd(x, y):
    raise NotImplementedError()


# Rekent het n-de getal van Fibonacci uit
def fibonacci(n):
    raise NotImplementedError()


# Rekent de som van de cijfers van n op
def sum_digits(n):
    raise NotImplementedError()


# Keer de cijfers van n om. Bv. 123 -> 321
def reverse_digits(n):
    raise NotImplementedError()


