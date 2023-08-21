# Генерация csv файла с тремя случайными
# числами в каждой строке. 100-1000 строк.

import csv
from random import randint

def csv_w_3_rand_nums(csv_name: str):
    with open(f"{csv_name}.csv", 'w', newline='') as file:
        list_for_writing = [[str(randint(1, 10)).strip() for i in range(3)] for j in range(100)]
        writer = csv.writer(file)
        for i in list_for_writing:
            writer.writerow(i)

csv_w_3_rand_nums('test')
