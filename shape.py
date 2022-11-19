from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, name):
        self.name_of_shape = name

    def __str__(self):
        pass

    def get_name(self):
        return self.name_of_shape

    def set_name(self, name):
        self.name_of_shape = name

    name = property(get_name, set_name)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        pass
