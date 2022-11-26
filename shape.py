from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """Shape is an abstract base class which other shapes can extend."""

    def __init__(self, name):
        self._name = name

    def __str__(self):
        """Returns a string representation of the current shape."""
        return f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}"

    @property
    def name(self):
        """Returns name of current shape."""
        return self._name

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


