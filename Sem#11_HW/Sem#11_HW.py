from random import randint
import numpy as np
class Matrix:
    """Create, compare, add and multiply matrixes"""

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def create_matrix(self):
        res = np.random.randint(0, 9, (self.row, self.col))
        return res

    def __add__(self, other):
        return self.create_matrix() + other.create_matrix()

    def __eq__(self, other):
        return self.create_matrix() == other.create_matrix()

    def __mul__(self, other):
        return self.create_matrix() * other.create_matrix()

a = Matrix(4, 4)
b = Matrix(4, 4)
print(a.create_matrix(), b.create_matrix(), a + b, a == b, a * b, sep='\n')
