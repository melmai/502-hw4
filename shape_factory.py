from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class ShapeFactory:

    @staticmethod
    def create_shape(shape_name, *shape_data):
        fix_name = shape_name.upper()
        if fix_name == "CIRCLE":
            new_shape = Circle(shape_name, *shape_data)
        elif fix_name == "SQUARE":
            new_shape = Square(shape_name, *shape_data)
        elif fix_name == "RECTANGLE":
            new_shape = Rectangle(shape_name, *shape_data)
        elif fix_name == "TRIANGLE":
            new_shape = Triangle(shape_name, *shape_data)
        else:
            raise TypeError("That is not a valid shape.")
        return new_shape
