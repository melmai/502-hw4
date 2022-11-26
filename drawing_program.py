class DrawingProgram:

    def __init__(self):
        self.list_of_shapes = []

    def __str__(self):
        """Returns a string representation of each of the shapes --
        each shape will be separated from others by a newline (\n)"""
        ret_string = ""
        for shape in self.list_of_shapes:
            ret_string += str(shape)
            ret_string += "\n"
        return ret_string

    def add_shape(self, shape):
        """A method that adds a Shape."""
        self.list_of_shapes.append(shape)

    def remove_shape(self, shape):
        """A method that removes ALL shapes that match the one passed as a
        parameter -- it should return in integer value to signify how many
        of that shape was removed"""
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

    def print_shape(self, shape_name):
        """Prints all shapes that match the type of the shape passed in."""
        for shape in self.list_of_shapes:
            if shape.name == shape_name:
                print(shape)

    def sort_shapes(self):
        """Sorts the list/collection of shapes -- you must use a sort that runs
        in O(nlogn) for its worst case shapes will be sorted first by name,
        then by area if names are same."""

        # if there are fewer than 2 shapes, there's nothing to sort
        # otherwise, use merge sort to sort the list
        if self.get_size() > 2:
            self.list_of_shapes = self.merge_sort(self.list_of_shapes)
        return

    def merge_sort(self, shapes_list):
        """Sorts the list of shapes recursively using merge sort."""
        if len(shapes_list) > 1:
            new_array = shapes_list

            # split the list
            mid_idx = len(shapes_list) // 2
            left_array = shapes_list[:mid_idx]
            right_array = shapes_list[mid_idx:]

            # call merge sort recursively
            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i = j = k = 0

            # merge sorted arrays
            while i < len(left_array) and j < len(right_array):

                # check first values and add the lowest one to the new array
                # then increment
                if left_array[i].name == right_array[j].name:
                    if left_array[i].area() < right_array[j].area():
                        new_array[k] = left_array[i]
                        i += 1
                    else:
                        new_array[k] = right_array[j]
                        j += 1
                elif left_array[i].name < right_array[j].name:
                    new_array[k] = left_array[i]
                    i += 1
                else:
                    new_array[k] = right_array[j]
                    j += 1

                # move on to the next element in the new array
                k += 1

            # add any leftover values from left array, if any exist
            while i < len(left_array):
                new_array[k] = left_array[i]
                i += 1
                k += 1

            # add any leftover values from right array, if any exist
            while j < len(right_array):
                new_array[k] = right_array[j]
                j += 1
                k += 1

            return new_array

    def get_shape(self, index):
        """Returns the shape at the specified index"""
        return self.list_of_shapes[index]

    def set_shape(self, index, shape):
        """Replaces the shape at the specified index"""
        self.list_of_shapes[index] = shape
    
    def get_size(self):
        """Returns the number of shapes in the list."""
        return len(self.list_of_shapes)

    def __iter__(self):
        return drawingProgramIterator(self)


class drawingProgramIterator:
    """ Iterator class """
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        """Returns the next value from DrawingProgram object's lists of
        shapes"""
        if self.index < len(self.collection.list_of_shapes):
            result = self.collection.list_of_shapes[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
