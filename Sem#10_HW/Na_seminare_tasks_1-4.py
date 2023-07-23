# from math import pi
#
# class Circle:
#
#     def __init__(self, radius: float) -> None:
#         self.radius = radius
#     def get_length(self) -> float:
#         return 2 * pi * self.radius
#
#     def get_area(self) -> float:
#         return pi * (self.radius) ** 2
#
# exp1 = Circle(3)
# print(exp1, exp1.get_length(), exp1.get_area())


# class Pryamougolnik:
#     def __init__(self, length: float, width: float | None) -> None:
#         self.length = length
#         if width:
#             self.width = width
#         else:
#             self.width = self.length
#
#     def get_perim(self) -> float:
#          return (self.length + self.width) * 2
#
#     def get_area(self) -> float:
#         return self.length * self.width
#
#     # def __str__(self) -> str:
#     #     return f'The P - {} and S - {get_area(self)}'
#
#
# exmp1 = Pryamougolnik(5, 6)
# print(exmp1.get_area(), exmp1.get_perim())


# class Person:
#
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self._age = age
#
#     def __str__(self):
#         return f'{self.name}, age: {self._age}'
#
#     def birthday(self):
#         self._age += 25
#
# class Employee(Person):
#     LEVEL_CONST = 7
#     def __init__(self, name: str, age: int, id: int) -> None:
#         super().__init__(name, age)
#         self.id = id
#         self.level = id % self.LEVEL_CONST
#
# empl1 = Employee('Johny Cage', 32, 222225)
# print(empl1, empl1.level)
#
# empl1.birthday()
# print(empl1, empl1.level)
