import time


class My_string(str):
    """The class is inherited from str,
    returns name and time of printing for
    both a user and a developer """

    def __new__(cls, author: str, value):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'Для пользователя {self.author}, {self.time}'

    def __repr__(self):
        return f'Для программиста {self.author}, {self.time}'


example1 = My_string('Name', 'Bob')
print(example1)
print(repr(example1))


class Rectangle:
    """This class compares the values of two rectangles and also
    returns addition, substraction, division and multiplication results"""
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

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

    def __eq__(self, other):
        return self.sq_area() == other.sq_area()

    def __ne__(self, other):
        return self.sq_area() != other.sq_area()

    def __gt__(self, other):
        return self.sq_area() > other.sq_area()

    def __ge__(self, other):
        return self.sq_area() >= other.sq_area()

    def __et__(self, other):
        return self.sq_area() < other.sq_area()

    def __le__(self, other):
        return self.sq_area() <= other.sq_area()


a = Rectangle(3, 4)
b = Rectangle(5, 6)

print(a + b, a - b, a * b, a / b, a == b, a != b, a < b, a > b, a >= b, a <= b, sep='\n')
