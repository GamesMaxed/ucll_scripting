class NamedLambda:
    def __init__(self, name, function):
        self._name = name
        self._function = function

    def __call__(self, *args, **kwargs):
        self._function(*args, **kwargs)

    def __str__(self):
        return self._name

    def __repr__(self):
        return "<function {}>".format(self._name)
        

def named_lambda(name, function):
    return NamedLambda(name, function)
