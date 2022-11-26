import math
from shape import Shape


class Circle(Shape):

    def __init__(self, name="Circle", radius=0.0):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self):
        print(self)