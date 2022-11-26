from unittest import TestCase
from drawing_program import DrawingProgram
from circle import Circle
from square import Square
from triangle import Triangle


class TestdrawingProgramIterator(TestCase):

    def test_for_no_shapes(self):
        list_for_test = []
        draw_obj = DrawingProgram()
        iterator = iter(draw_obj)
        for shapes in draw_obj:
            list_for_test.append(shapes)
        self.assertEqual(list_for_test, [])

    def test_for_one_shape(self):
        list_for_test = []
        draw_obj = DrawingProgram()
        shape_circle = Circle("circle", 2)
        draw_obj.add(shape_circle)
        iterator = iter(draw_obj)
        for shapes in draw_obj:
            list_for_test.append(shapes)
        self.assertEqual(list_for_test, [shape_circle])

    def test_for_five_shapes(self):
        list_for_test = []
        draw_obj = DrawingProgram()
        shape_circle1 = Circle("circle1", 2)
        shape_square1 = Square("square1", 4)
        shape_circle2 = Circle("circle1", 4)
        shape_square2 = Square("square1", 5)
        shape_circle3 = Circle("circle3", 8)
        draw_obj.add_shape(shape_circle1)
        draw_obj.add_shape(shape_square1)
        draw_obj.add_shape(shape_circle2)
        draw_obj.add_shape(shape_square2)
        draw_obj.add_shape(shape_circle3)
        iterator = iter(draw_obj)
        for shapes in draw_obj:
            list_for_test.append(shapes)
        self.assertEqual(list_for_test, [shape_circle1, shape_square1, shape_circle2, shape_square2, shape_circle3])


if __name__ == '__main__':
    TestCase.main()
