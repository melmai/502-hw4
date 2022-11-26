from shape import Shape
import math


class Triangle(Shape):
    def __init__(self, name="Triangle", side_one=0.0, side_two=0.0, side_three=0.0):
        super().__init__(name)
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three

    def area(self):
        return 0.25 * math.sqrt((4 * self.side_one ** 2 * self.side_two ** 2) -
                                (self.side_one ** 2 + self.side_two ** 2 - self.side_three ** 2) ** 2)

    def perimeter(self):
        return self.side_one + self.side_two + self.side_three

    def draw(self):
        print(self)
