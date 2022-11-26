from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class ShapeFactory:
    """Class that will create shapes"""

    @staticmethod
    def create_shape(shape_name, *shape_data):
        """creates shapes and their dimensions based on user input"""
        if shape_name == "circle":
            new_shape = Circle(shape_name, *shape_data)
        elif shape_name == "square":
            new_shape = Square(shape_name, *shape_data)
        elif shape_name == "rectangle":
            new_shape = Rectangle(shape_name, *shape_data)
        elif shape_name == "triangle":
            new_shape = Triangle(shape_name, *shape_data)
        else:
            raise TypeError("That is not a valid shape. Please have no capital letters in the shape name.")
        return new_shape