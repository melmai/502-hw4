from unittest import TestCase
from shape import Shape


class TestShape(TestCase):
    def test_init(self):
        my_shape = Shape()
        self.assertEqual("", my_shape.__str__(), "shape should be empty, but is not")

    def test_get_name(self):
        my_shape = Shape("Rectangle")
        self.assertEqual("Rectangle", my_shape.get_name(), "correct name not returned")

    def test_set_name(self):
        my_shape = Shape("Rectangle")
        self.assertEqual("Rectangle", my_shape.set_name("Square"))

    def test_area(self):
        self.fail()

    def test_perimeter(self):
        self.fail()

    def test_draw(self):
        self.fail()
