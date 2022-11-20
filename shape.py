from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}"

    @property
    def name(self):
        """Get the name of the current shape."""
        return self.name

    @abstractmethod
    def area(self):
        """Get the area of the current shape."""

    @abstractmethod
    def perimeter(self):
        """Get the perimeter of the current shape."""

    @abstractmethod
    def draw(self):
        """Prints the name of the shape followed by the area and perimeter of the shape."""
        print(self)
