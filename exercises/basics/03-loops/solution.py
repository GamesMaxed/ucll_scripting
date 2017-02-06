def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return n > 1


def count_primes_below(n):
    count = 0

    for i in range(0, n):
        if is_prime(i):
            count += 1

    return count


def gcd(x, y):
    x = abs(x)
    y = abs(y)

    for i in range(max(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i

    return 0


def fibonacci(n):
    a = 0
    b = 1

    while n != 0:
        a, b = b, a + b
        n -= 1

    return a


def sum_digits(n):
    result = 0

    n = abs(n)
    while n > 0:
        result += n % 10
        n = n // 10

    return result


def reverse_digits(n):
    result = 0

    if n < 0:
        return -reverse_digits(-n)
    else:
        while n > 0:
            result = result * 10 + (n % 10)
            n = n // 10

        return result

