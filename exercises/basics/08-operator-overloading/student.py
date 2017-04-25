class Fraction:
    def __gcd(self, x: float, y: float):
        if x < 0:
            return self.__gcd(-x, y)
        elif y < 0:
            return self.__gcd(x, -y)
        elif y == 0:
            return x
        else:
            return self.__gcd(y, x % y)

    def __init__(self, numerator: float, denominator: float):
        if denominator == 0:
            raise RuntimeError('Denominator must not be 0')
        else:
            gcd = self.__gcd(numerator, denominator)

            if denominator < 0:
                numerator = -numerator
                denominator = -denominator

            self.__numerator = numerator / gcd
            self.__denominator = denominator / gcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, that):
        numerator = self.numerator * that.numerator
        denominator = self.denominator * that.denominator

        return Fraction(numerator, denominator)

    def invert(self):
        return Fraction(self.denominator, self.numerator)

    def __truediv__(self, other):
        return self * other.invert()

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

