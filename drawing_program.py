
class DrawingProgram:

    def __init__(self):
        self.list_of_shapes = []

    def __str__(self):
        """returns a string representation of each of the shapes --
        each shape will be separated from others by a newline (\n)"""
        pass

    def add_shape(self, shape):
        """A method that adds a Shape"""
        self.list_of_shapes.append(shape)

    def remove_shape(self, shape):
        """A method that removes ALL shapes that match the one passed as a parameter --
        it should return in integer value to signify how many of that shape was removed"""
        shape_count = 0
        for shapes in self.list_of_shapes:
            if shapes == shape:
                self.list_of_shapes.remove()
                shape_count += 1
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

    def __iter__(self):
        return drawingProgramIterator(self)


class drawingProgramIterator:
    """ Iterator class """
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        """Returns the next value from DrawingProgram object's lists of shapes"""
        if self.index < len(self.collection.list_of_shapes):
            result = self.collection.list_of_shapes[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


