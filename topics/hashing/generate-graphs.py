import matplotlib.pyplot as plt
import functools
import math


def ordinal(x):
    return ord(x) - ord('a')

def unordinal(x):
    return chr(x + ord('a'))

def string_prefix_hash(n):
    def hash(string):
        return functools.reduce(lambda acc, x: acc * 26 + ordinal(x), string[0:n], 0)

    return hash

def string_length_hash(n):
    def hash(string):
        return len(string)

    return hash

def string_sum_hash(n):
    def hash(string):
        return sum( ordinal(c) for c in string )

    return hash

def unhash(h, n):
    if n == 0:
        return ""
    else:
        rest = h % 26
        return unhash((h - rest) // 26, n-1) + unordinal(rest)

def load_dictionary():
    with open('fnames.txt', 'r') as file:
        return [ line.strip().lower() for line in file ]

dictionary = load_dictionary()
    
def hashes(hash_function):
    return [ hash_function(word) for word in dictionary ]

def hash_frequencies(hash_function):
    result = dict()

    for word in dictionary:
        h = hash_function(word)
        result[h] = result.get(h, 0) + 1

    return result



plt.hist(hashes(string_prefix_hash(1)), bins=26)
plt.savefig('prefix1.png')
plt.clf()

plt.hist(hashes(string_prefix_hash(2)), bins=676)
plt.savefig('prefix2.png')
plt.clf()

plt.hist(hashes(string_prefix_hash(3)), bins=1000)
plt.savefig('prefix3.png')
plt.clf()

plt.hist(hashes(string_length_hash(3)))
plt.savefig('length.png')
plt.clf()

plt.hist(hashes(string_sum_hash(3)), bins=200)
plt.savefig('sum.png')
plt.clf()

plt.hist( [ int(1000/x**0.2) for x in range(1, 1000) ], bins=100 )
plt.savefig('uneven.png')
plt.clf()

plt.hist( [ x + 5 * math.sin(x) for x in range(1, 1000) ], bins=100)
plt.ylim((0,50))
plt.savefig('uniform.png')
plt.clf()
