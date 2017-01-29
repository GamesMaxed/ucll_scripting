def to_binary(n):
    if n < 0:
        raise RuntimeError("n must be positive")
    elif n == 0:
        return "0"
    else:
        result = ""

        while n > 0:
            result = str(n % 2) + result
            n = n // 2

        return result
