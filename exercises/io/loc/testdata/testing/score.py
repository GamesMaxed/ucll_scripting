class Score:
    """
    Represents a score.

    Scores are not to be confused with fractions.
    For example, a score of 5/10 is not the same as a score of 1/2.
    Score addition also follows different rules.
    """
    def __init__(self, value, maximum):
        assert 0 <= value, "Score value must be positive"
        assert value <= maximum, "Score value ({}) must not be greater than maximum ({})".format(value, maximum)
        
        self.value = value
        self.maximum = maximum

    def __add__(self, other):
        """
        Adds two scores together.

        a/b + c/d = (a+c)/(b+d).
        """
        return Score(self.value + other.value, self.maximum + other.maximum)

    def rescale(self, maximum):
        """
        Rescales the score to a given maximum.
        """
        return Score(self.value / self.maximum * maximum, maximum)

    def __str__(self):
        return "{}/{}".format(self.value, self.maximum)

    def is_max_score(self):
        return self.value == self.maximum
