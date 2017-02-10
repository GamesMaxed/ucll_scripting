def count_common_chars(s1, s2):
    return sum( 1 for c1, c2 in zip(s1, s2) if c1 == c2 )


def hack(candidates, attempt):
    while len(candidates) > 1:
        candidate = candidates[0]
        n = attempt(candidate)
        
        if n == len(candidate):
            return candidate

        candidates = [ c for c in candidates if count_common_chars(c, candidate) == n ]

    return candidates[0]
