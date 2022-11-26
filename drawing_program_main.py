from drawing_program import DrawingProgram
from drawing_program import drawingProgramIterator
from circle import Circle
from square import Square
from triangle import Triangle


class DrawingProgramMain:
    if __name__ == '__main__':
        draw_obj = DrawingProgram()
        shape_circle1 = Circle("circle1", 2)
        shape_square1 = Square("square1", 4)
        shape_triangle1 = Triangle()
        shape_circle2 = Circle("circle1", 4)
        shape_square2 = Square("square1", 5)
        draw_obj.add_shape(shape_circle1)
        draw_obj.add_shape(shape_square1)
        draw_obj.add_shape(shape_triangle1)
        draw_obj.add_shape(shape_circle2)
        draw_obj.add_shape(shape_square2)
        print(draw_obj)
        draw_obj.sort_shapes()
        print(draw_obj)
        shape_circle3 = Circle("circle3", 8)
        shape_square3 = Square("square3", 3)
        shape_triangle2 = Triangle()
        draw_obj.add_shape(shape_circle3)
        draw_obj.add_shape(shape_square3)
        draw_obj.add_shape(shape_triangle2)
        print(draw_obj)
        shape_square4 = Square("square4", 1)
        draw_obj.set_shape(3, shape_square3)
        draw_obj.set_shape(7, shape_circle1)
        draw_obj.set_shape(1, shape_square4)
        print(draw_obj)
        draw_obj.sort_shapes()
        print(draw_obj)



