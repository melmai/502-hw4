from drawing_program import DrawingProgram
from shape_factory import ShapeFactory
from drawing_program import drawingProgramIterator
from circle import Circle
from square import Square
from triangle import Triangle


class DrawingProgramMain:
    if __name__ == '__main__':
        my_shapes = DrawingProgram()
        for i in range(0, 3):
            my_shapes.add_shape(ShapeFactory.create_shape("square", 2.0))
        my_shapes.add_shape(ShapeFactory.create_shape("rectangle", 2.0, 4.0))
        for i in range(0, 2):
            my_shapes.add_shape(ShapeFactory.create_shape("triangle", 3.0, 4.0, 5.0))
        my_shapes.add_shape(ShapeFactory.create_shape("circle", 3.0))
        print(my_shapes.get_shape(6))
        #my_shapes.sort_shapes()
        iterator = iter(my_shapes)
        for shapes in my_shapes:
            print(shapes)
        my_shapes.add_shape(ShapeFactory.create_shape("circle", 5.0))
        my_shapes.add_shape(ShapeFactory.create_shape("rectangle", 1.0, 3.0))
        my_shapes.set_shape(2, ShapeFactory.create_shape("circle", 4.0))
        # my_shapes.sort_shapes()
        for shapes in my_shapes:
            print(shapes)
        print(my_shapes.remove_shape(Square()))



