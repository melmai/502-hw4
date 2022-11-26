from shape import Shape

class Square(Shape):

    def __init__(self, name="Square", length=0):
        super().__init__(name)
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4

    def draw(self):
        print(self)
