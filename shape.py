from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """Returns a string representation of the current shape."""
        return f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}"

    @property
    def get_name(self):
        return self.name

    @property
    def set_name(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Get the area of the current shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Get the perimeter of the current shape."""
        pass

    @abstractmethod
    def draw(self):
        """Prints the name of the shape followed by the area and perimeter of the shape."""
        pass
