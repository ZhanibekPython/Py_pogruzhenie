"""Не смог создать последовательность чтоб она делилась на списки. Если набрать мматрицу вручную,
тогда все норм работает. Но тогда какой смысл делать функцию если ее повторно нельзя будет использовать"""

def matrix_transpose(streak: int = 3, col: int = 3) -> list[[]]:
    """Returns transponed matrix"""
    #start = [[0] * streak for i in range(col)]
    start = [[i] * streak for i in range(col)]
    matrix = [[0] * streak for i in range(col)]
    for i in range(len(start)):
        for j in range(len(start[0])):
            matrix[i][j] = start[j][i]
    return matrix

print(*matrix_transpose())


def matrix_reload(streak: int = 3, col: int = 3) -> list[[]]:
    """Returns transponed matrix (shorted code version)"""
    start = [[i] * streak for i in range(col)]
    return [[start[j][i] for j in range(len(start))] for i in range(len(start[0]))]

print(matrix_reload(6, 6))


def matrix_revolution(streak: int = 3, col: int = 3) -> list[[]]:
    """Returns transponed matrix (by zip())"""
    start = ([i] * streak for i in range(col))
    zip_matrix = zip(*start)
    matrix = [list(i) for i in zip_matrix]
    return matrix

print(matrix_revolution())
