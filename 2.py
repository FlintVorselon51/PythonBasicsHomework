from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def calculate_costs(self):
        pass


class Coat(Clothing):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def calculate_costs(self):
        return self.size / 6.5 + 0.5


class Suit(Clothing):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def calculate_costs(self):
        return self.height * 2 + 0.3


coat = Coat('Пальто', 13)
suit = Suit('Костюм', 5)

print(coat.calculate_costs)
print(suit.calculate_costs)
