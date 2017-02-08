def inverse_lookup(xs):
    result = dict()

    for i in range(0, len(xs)):
        x = xs[i]

        if x not in result:
            result[x] = i

    return result


def get_with_default(map, key, default):
    if key in map:
        return map[key]
    else:
        return default

# Kortere oplossing (functionaliteit is reeds ingebouwd in Python dicts)
def get_with_default(map, key, default):
    return map.get(key, default)


def count_frequencies(xs):
    result = dict()

    for x in xs:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1

    return result


def css_lookup(stylesheets, key, default):
    for stylesheet in stylesheets:
        if key in stylesheet:
            return stylesheet[key]

    return default


def word_width(letter_widths, word):
    return sum( letter_widths[letter] for letter in word )


def group_by_extension(filenames):
    result = dict()

    for filename in filenames:
        extension = filename[-3:]

        if extension not in result:
            result[extension] = []

        result[extension].append(filename)

    return result
