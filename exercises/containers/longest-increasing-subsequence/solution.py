def longest_increasing_subsequence(xs):
    if len(xs) == 0:
        return []
    else:
        longest = []
        current = [xs[0]]
    
        for x in xs[1:]:
            if x < current[-1]:
                current = []
                
            current.append(x)

            if len(current) > len(longest):
                longest = current

        return longest
