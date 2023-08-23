# import json
# class Factorial:
#
#     def __init__(self, fact: int, arch_num: int):
#         self.fact = fact
#         self.arch_num = arch_num
#         self.archieve = []
#
#     def __call__(self, k: int):
#         res = 1
#         for i in range(1, self.fact + 1):
#             res *= i
#             self.archieve.append({i: res})
#         while len(self.archieve) > self.arch_num:
#             self.archieve.pop(0)
#         return res
#
#
#     def callArchieve(self):
#         return self.archieve[:self.arch_num] if self.arch_num < len(self.archieve) else self.archieve
#
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         with open('result.json', 'w') as file:
#             json.dump(self.archieve, file, indent = 4)
#
# # ex1 = Factorial(5, 3)
# # print(ex1(5), ex1.callArchieve())
# #
# # ex1 = Factorial(8, 5)
# # print(ex1(8), ex1.callArchieve())
# #
# # get_fact = Factorial(5, 4)
# # with get_fact as res:
# #     get_fact(5)


# class FactNumGen:
#
#     def __init__(self, stop: int, start: int = 1, step: int = 1):
#         self.stop = stop
#         self.start = start
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         res = 1
#         for num in range(self.start, self.stop + 1, self.step):
#             res *= num
#             return res
#         raise StopIteration
#
#
#
#
# ex2 = FactNumGen(10, 2)
# for i in ex2:
#     print(i)


class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value <= 0:
            raise ValueError('Число должно быть больше 0')

class Rectangle:
    __slots__ =  ('_width', '_length')

    width = Range()
    length = Range()

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    # @property
    # def length(self):
    #     return self._length
    #
    # @length.setter
    # def length(self, value):
    #     self._length = value
    #
    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, value):
    #     self._width = value

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


rect = Rectangle(3, 5)

rect.width = 5

print(rect.width)
