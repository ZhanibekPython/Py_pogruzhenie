import unittest
import pytest


class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    @classmethod
    def validate(cls, value):
        if value <= 0:
            raise ValueError('Число должно быть больше 0')


class Rectangle:
    """
    Returns P and S of a rectangle

    """

    width = Range()
    length = Range()

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length
        self.perimeter()

    def test_per_rectangles(self, other):
        return self == other

    def sq_area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    def __sub__(self, other):
        return abs(self.perimeter() - other.perimeter())

    def __mul__(self, other):
        return self.sq_area() * other.sq_area()

    def __truediv__(self, other):
        return self.sq_area() / other.sq_area() if (self.sq_area() > other.sq_area()) else (
                other.sq_area() / self.sq_area())

    def __str__(self):
        return f"{(self.width + self.length) * 2}"


# class TestRectangle(unittest.TestCase):
#     def setUp(self) -> None:
#         self.rec1 = Rectangle(1, 1)
#         self.rec2 = Rectangle(2, 2)
#         self.rec3 = Rectangle(2, 4)
#
#     def test_false(self):
#         self.assertFalse(self.rec3, self.rec1+self.rec2+1)
#
#     def test_isequal(self):
#         self.assertEqual(4, self.rec2.sq_area())
#
#     def test_istrue(self):
#         self.assertTrue((self.rec1 + self.rec3) == 16, 'неверно')
#
#
# if __name__ == '__main__':
#     unittest.main()

rec1 = Rectangle(1, 1)

rec3 = Rectangle(2, 2)
rec2 = Rectangle(2, 4)


def test_compare_rectangles():
    assert rec1 == rec2
    assert rec2 == rec3