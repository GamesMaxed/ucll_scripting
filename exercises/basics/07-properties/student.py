class Person:
    def __init__(self, weight, length):
        __weight = 0
        __height = 0
        self.weight = weight
        self.height = length

    # Weight getter
    @property
    def weight(self):
        return self.__weight

    # Weight setter
    @weight.setter
    def weight(self, value):
        if value < 0:
            raise RuntimeError()
        self.__weight = value

    # Height getter
    @property
    def height(self):
        return self.__height

    # Height setter
    @height.setter
    def height(self, value):
        if value < 0:
            raise RuntimeError()
        self.__height = value


    # Bmi getter
    @property
    def bmi(self):
        return self.weight / self.height ** 2
