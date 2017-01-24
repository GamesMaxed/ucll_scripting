class Person:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise RuntimeError("Invalid weight")
        else:
            self.__weight = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise RuntimeError("Invalid height")
        else:
            self.__height = value

    @property
    def bmi(self):
        return self.weight / self.height ** 2
