from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, name):
        self.name_of_shape = name

    def __str__(self):
        pass

    def get_name(self):
        return self.name_of_shape

    def set_name(self, name):
        self.name_of_shape = name

    name = property(get_name, set_name)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        """Prints the name of the shape followed by the area and perimeter of the shape"""
        print(
            f"{self.name_of_shape}, area: {self.area()}, perimeter: {self.perimeter()}")
