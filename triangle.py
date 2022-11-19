from shape import Shape


class Triangle(Shape):
    def __init__(self, name, side_one, side_two, side_three):
        super().__init__(name)
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three

    def area(self):
        pass

    def perimeter(self):
        return self.side_one + self.side_two + self.side_three
