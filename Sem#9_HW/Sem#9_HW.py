import csv
import json
from functools import wraps
from random import randint


def csv_w_3_rand_nums(csv_name: str):
    """Creates 100 rows with three random digits in it"""
    with open(f"{csv_name}.csv", 'w', newline='') as file:
        list_for_writing = [[str(randint(1, 10)).strip() for i in range(3)] for j in range(100)]
        writer = csv.writer(file)
        for i in list_for_writing:
            writer.writerow(i)


def quadro_equal_decor(func: callable) -> callable:
    """Inserts three random numbers from preprepared CSV-file into a func"""

    @wraps(func)
    def decor_itself(*args):
        try:
            with open(f"{func.__name__}.csv", 'r') as src:
                data = src.read()
        except FileNotFoundError:
            with open(f"{func.__name__}.csv", 'w') as src:
                writer = csv.writer(src)
                data =
                for i in data:
                    args = i
                    func(i)

    return decor_itself


def res_to_json(func: callable, *args) -> callable:
    """Saves incoming parameters and the result of the func work into a JSON-file"""
    @wraps(func)
    def deco(*args, **kwargs):
        with open(f"{func.__name__}.json", 'r') as file:
            data = json.load(file)
        with open(f"{func.__name__}.json", 'w') as file:
            data = {'args': args, 'res': res_to_json(*args)}
            json.dump(data, file, indent=4)

@res_to_json
@csv_w_3_rand_nums
@quadro_equal_decor
def quadro_equal(b, a, c):
    """Simple quodratic equations solving func"""
    discr = b ** 2 - (4 * a * c)
    root1 = (-b + discr * 0.5) / 2 * a
    root2 = (-b - discr * 0.5) / 2 * a
    if discr < 0: return "Уравнение не имеет корней!"
    if discr == 0: return root1
    return [root1, root2]

quadro_equal(4, 2, 1)