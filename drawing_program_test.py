from drawing_program import DrawingProgram
from shape_factory import ShapeFactory

def test_drawing_program():

    # create drawing program
    print("Creating drawing program...")
    drawing_program = DrawingProgram()

    # create shapes and add to drawing program
    print("Adding shapes to drawing program...")
    circle = ShapeFactory.create_shape("Circle", 2.0)
    drawing_program. add_shape(circle)

    rectangle = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
    drawing_program. add_shape(rectangle)

    square = ShapeFactory.create_shape("Square", 2.0)
    drawing_program. add_shape(square)

    triangle = ShapeFactory.create_shape("Triangle", 5.0, 6.0, 7.0)
    drawing_program. add_shape(triangle)

    # print all shapes
    print("All shapes in drawing program:")
    print(drawing_program)

    # get 1st shape
    print(f"First shape: {drawing_program.get_shape(0)}")

    # get 2nd shape
    print(f"Second shape: {drawing_program.get_shape(1)}")

    # Sort shapes
    print("Sorting shapes...")
    drawing_program.sort_shapes()

    # Print sorted shapes
    print(drawing_program)

    # replace shape
    new_circle = ShapeFactory.create_shape("Circle", 5.0)

    print("Replacing last shape...")
    drawing_program.set_shape(3, new_circle)

    print(drawing_program)

    # remove all circles
    print("Removing all circles from drawing program...")
    drawing_program.remove_shape("Circle")

    print("Circles removed.")
    print(drawing_program)


test_drawing_program()
