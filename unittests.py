import unittest
from shape_factory import ShapeFactory
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


class ShapeFactorTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.test_shape_factory = ShapeFactory()

    def testCreate_shape_circle(self):
        self.assertIsInstance(self.test_shape_factory.create_shape("circle", 4.0), Circle,
                              "The factory did not create a circle.")

    def testCreate_shape_rectangle(self):
        self.assertIsInstance(self.test_shape_factory.create_shape("rectangle", 5.0, 6.0), Rectangle,
                              "The factory did not create a rectangle.")

    def testCreate_shape_square(self):
        self.assertIsInstance(self.test_shape_factory.create_shape("square", 4.0), Square,
                              "The factory did not create a square.")

    def testCreate_shape_triangle(self):
        self.assertIsInstance(self.test_shape_factory.create_shape("triangle", 3.0, 5.0, 7.0), Triangle,
                              "The factory did not create a triangle.")

    @unittest.expectedFailure
    def testCreate_shape_wrong_shape(self):
        list_of_shapes = [Circle(), Rectangle(), Square(), Triangle()]
        self.assertIsInstance(self.test_shape_factory.create_shape("oval", 5.0), list_of_shapes,
                              "The factory created a valid shape.")


unittest.main()
