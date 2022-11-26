from drawing_program import DrawingProgram
from shape_factory import ShapeFactory

def test_drawing_program():

    # create drawing program
    print("Creating drawing program...")
    drawing_program = DrawingProgram()
    
    print(f"Drawing program created! Number of shapes: "
          f"{drawing_program.get_size()}\n")

    # create shapes and add to drawing program
    print("Creating 4 shapes...")
    circle = ShapeFactory.create_shape("Circle", 2.0) 
    rectangle = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
    square = ShapeFactory.create_shape("Square", 2.0)
    triangle = ShapeFactory.create_shape("Triangle", 5.0, 6.0, 7.0)

    print("Adding shapes to drawing program...")
    drawing_program.add_shape(circle)
    drawing_program.add_shape(rectangle)
    drawing_program.add_shape(square)
    drawing_program.add_shape(triangle)
    print(
        f"Number of shapes: {drawing_program.get_size()}\n")

    # print all shapes
    print("All shapes in drawing program:")
    print(drawing_program)

    # get 1st shape
    print(f"First shape: {drawing_program.get_shape(0)}")

    # get 2nd shape
    print(f"Second shape: {drawing_program.get_shape(1)} \n")

    # Sort shapes
    print("Sorting shapes...\n")
    drawing_program.sort_shapes()

    # Print sorted shapes
    print("Sorted shapes:")
    print(drawing_program)

    # replace shape
    print("Creating new circle shape...")
    new_circle = ShapeFactory.create_shape("Circle", 5.0)
    print("Circle created!")
    print(new_circle)
    print()

    print("Replacing last shape...\n")
    drawing_program.set_shape(3, new_circle)

    print("New shape list:")
    print(drawing_program)

    # Sort shapes
    print("Sorting shapes...\n")
    drawing_program.sort_shapes()

    # Print sorted shapes
    print("Sorted shapes:")
    print(drawing_program)

    # remove square shape
    print("Removing square from drawing program...")
    print(f"{drawing_program.remove_shape(square)} square removed.\n")
    
    print("Updated shapes in drawing program:")
    print(drawing_program)

    # remove circle shape type
    print("Removing all circles from drawing program...")
    print(f"{drawing_program.remove_shape_type('Circle')} circles removed.\n")

    print("Updated shapes in drawing program:")
    print(drawing_program)


test_drawing_program()
