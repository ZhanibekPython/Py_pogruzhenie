import unittest
import doctest
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
    # >>> rec1.sq_area()
    # 24
    #
    # >>> rec1.perimeter()
    # 20
    #
    # >>> rec1.perimeter() <  rec1.sq_area()
    # True
    #
    # >>> rec3.sq_area() == rec1.sq_area() + 11
    # True
    #
    # >>> rec1.perimeter() + rec2.perimeter() + rec3.perimeter()
    # 60
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

    @staticmethod
    def sum_p_and_s(first: int, second: int) -> int:
        per = (first + second) * 2
        sqr = first * second
        return per + sqr


def test_compare_sq_area():
    assert rec1.sq_area() == rec2.sq_area() + 8


def test_compare_perimeters():
    assert rec2.perimeter() == rec3.perimeter() - 8


@pytest.mark.parametrize('first, second, exp_res', [(4, 5, 38), (6, 7, 68), (2, 3, 16)])
def test_rect(first, second, exp_res):
    assert rec1.sum_p_and_s(first=first, second=second) == exp_res


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rec1 = Rectangle(1, 1)
        self.rec2 = Rectangle(2, 2)
        self.rec3 = Rectangle(2, 4)

    def test_false(self):
        self.assertFalse(self.rec3, self.rec1 + self.rec2 + 1)

    def test_isequal(self):
        self.assertEqual(4, self.rec2.sq_area())

    def test_istrue(self):
        self.assertTrue((self.rec1 + self.rec3) == 16, 'неверно')


rec1 = Rectangle(4, 6)
rec3 = Rectangle(5, 7)
rec2 = Rectangle(4, 4)

if __name__ == '__main__':
    unittest.main()
    doctest.testmod()
    pytest.main()
