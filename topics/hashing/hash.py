class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __hash__(self):
        return \
            self.h + \
            self.m + \
            self.s

    def __eq__(self, other):
        return \
            self.h == other.h and \
            self.m == other.m and \
            self.s == other.s
