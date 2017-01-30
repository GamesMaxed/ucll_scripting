class Fraction:
    def __gcd(self, x, y):
        if x < 0:
            return self.__gcd(-x, y)
        elif y < 0:
            return self.__gcd(x, -y)
        elif y == 0:
            return x
        else:
            return self.__gcd(y, x % y)

    def __init__(self, numerator, denominator):
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

    def __add__(self, that):
        numerator = self.numerator * that.denominator + that.numerator * self.denominator
        denominator = self.denominator * that.denominator

        return Fraction(numerator, denominator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    
    def __sub__(self, that):
        return self + -that

    def __mul__(self, that):
        numerator = self.numerator * that.numerator
        denominator = self.denominator * that.denominator
        
        return Fraction(numerator, denominator)

    def invert(self):
        return Fraction(self.denominator, self.numerator)

    def __div__(self, that):
        return self * that.invert()

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
