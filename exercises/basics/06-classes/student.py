class Counter:
    # Constructor
    def __init__(self):
        self.__x = 0

    def current(self):
        return self.__x

    def increment(self):
        self.__x += 1

    def reset(self):
        self.__x = 0
