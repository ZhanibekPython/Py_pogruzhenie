from sys import exit


def chess():
    N = 8

    matrix = [[0] * N for i in range(N)]
    for i in range(N):
        x, v = map(int, input("Введите координаты положения восьми ферзей: ").split())
        matrix[x-1][v-1] = 1

    flag = True

    def stop_iter():
        global flag
        flag = False
        print(flag)
        sys.exit()

    for i in range(N):
        count_i = 0
        count_j = 0
        for j in range(N):
            if matrix[i].count(1) >= 2:
                stop_iter()
            elif matrix[j].count(1) >= 2:
                stop_iter()
            elif matrix[i][j+1] == 1:
                count_i += 1
                if count_i > 1:
                    stop_iter()
            elif matrix[j][x+1] == 1:
                count_j += 1
                if count_j > 1:
                    stop_iter()

    print(flag)
