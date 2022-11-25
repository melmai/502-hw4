class DrawingProgram:

    def __init__(self):
        self.list_of_shapes = []

    def __str__(self):
        """returns a string representation of each of the shapes --
        each shape will be separated from others by a newline (\n)"""
        ret_string = ""
        for shape in self.list_of_shapes:
            ret_string += shape
        return ret_string

    def add_shape(self, shape):
        """A method that adds a Shape"""
        self.list_of_shapes.append(shape)

    def remove_shape(self, shape):
        """A method that removes ALL shapes that match the one passed as a parameter --
        it should return in integer value to signify how many of that shape was removed"""
        shape_count = 0
        shape_count_track = 0
        for shapes in self.list_of_shapes:
            if shapes.name == shape.name:
                shape_count_track += 1
        try:
            while shape_count < shape_count_track:
                for shapes in self.list_of_shapes:
                    if shapes.name == shape.name:
                        self.list_of_shapes.remove(shapes)
                        shape_count += 1
        except ValueError:
            pass
        return shape_count

    def print_shape(self, shape):
        """prints all shapes that match the type of the shape passed in"""
        pass

    def sort_shapes(self):
        """sorts the list/collection of shapes -- you must use a sort that runs in O(nlogn) 
        for its worst case shapes will be sorted first by name, then by area if names are same"""
        pass

    def get_shape(self, index):
        """returns the shape at the specified index"""
        return self.list_of_shapes[index]

    def set_shape(self, index, shape):
        """replaces the shape at the specified index"""
        self.list_of_shapes[index] = shape


class drawingProgramIterator:
    pass
