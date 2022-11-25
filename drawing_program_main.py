from drawing_program import DrawingProgram
from shape_factory import ShapeFactory
from circle import Circle
from square import Square

my_shapes = DrawingProgram()
for i in range(0, 10):
    my_shapes.add_shape(ShapeFactory.create_shape("Square", 2.0))
#print(my_shapes.get_shape(9))
print(my_shapes.remove_shape(Square()))
#print(my_shapes.get_shape(0))