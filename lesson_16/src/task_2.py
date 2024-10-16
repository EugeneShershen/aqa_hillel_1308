from abc import ABC, abstractmethod
from cmath import sqrt, pi


class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        result = (f'\nArea of the {type(self).__name__}: {self.get_area()}\n'
                  f'Perimeter of the {type(self).__name__}: {self.get_perimeter()}')

        return result


class Square(Shape):

    def __init__(self, side):
        self.__side = side

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)) is not True:
            raise TypeError("Side must be a number")
        if value <= 0:
            raise ValueError("Side must be more than 0")

        super().__setattr__(key, value)

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return self.__side * 4


class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)) is not True:
            raise TypeError("Side must be a number")
        if value <= 0:
            raise ValueError("Side must be more than 0")

        super().__setattr__(key, value)

    def get_area(self):
        p = self.get_perimeter() / 2
        return sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))

    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)) is not True:
            raise TypeError("Radius must be a number")
        if value <= 0:
            raise ValueError("Radius must be more than 0")

        super().__setattr__(key, value)

    def get_area(self):
        return pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self.__radius
