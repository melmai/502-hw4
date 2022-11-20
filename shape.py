from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        pass

    @property 
    def name(self):
        """Gets the name of the current shape"""
        return self.name

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
