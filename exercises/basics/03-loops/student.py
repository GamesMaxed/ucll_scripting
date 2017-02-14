def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


def count_primes_below(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count


def biggest_of_two(x, y):
    if x < y:
        return y
    return x


def gcd(x, y):
    x = abs(x)
    y = abs(y)

    for i in range(max(x, y), 0, -1):
        if x % i is 0 and y % i is 0:
            return i

    return 0


# Rekent het n-de getal van Fibonacci uit
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Rekent de som van de cijfers van n op
def sum_digits(n):
    som = 0
    n = abs(n)

    while n > 0:
        som += n % 10
        n //= 10

    return som


# Keer de cijfers van n om. Bv. 123 -> 321
def reverse_digits(n):
    result = ""

    for char in str(abs(n)):
        result = char + result

    if n < 0:
        result = "-" + result

    return int(result)
