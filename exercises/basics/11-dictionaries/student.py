def inverse_lookup(xs):
    result = dict()

    for i in range(0, len(xs)):
        x = xs[i]

        if x not in result:
            result[x] = i

    return result


def get_with_default(map, key, default):
    raise NotImplementedError()


def count_frequencies(xs):
    raise NotImplementedError()


def css_lookup(stylesheets, key, default):
    raise NotImplementedError()


def group_by_extension(filenames):
    """
    Gegeven een lijst filenames waarvan de 3 laatste tekens
    de extensie vormen, groepeer de bestandsnamen per extensie
    in een dictionary.
    De keys in de dictionary zijn de extensies,
    de bijhorende waarde is een lijst van bestandsnamen
    met die extensie.
    
    Bv. [ 'foo.txt', 'bar.txt', 'baz.png' ]
    moet de dictionary
      { 'txt': [ 'foo.txt', 'bar'txt' ],
        'png': [ 'baz.png' ] }
    opleveren.
    """
    raise NotImplementedError()
