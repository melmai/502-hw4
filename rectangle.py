from shape import Shape 


class Rectangle(Shape):

    def __init__(self, name="Rectangle", length=0.0, width=0.0):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def draw(self):
        print(self)
