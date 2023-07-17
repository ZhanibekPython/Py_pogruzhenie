from random import randint
import json
from functools import wraps


def guess_num(num: int, tries: int) -> callable:
    def guess() -> bool:
        for _ in range(tries):
            user_num = int(input('Guess the number: '))
            if user_num == num:
                print('That is it. Good job!')
                return True
            elif user_num > num:
                print('Lower')
            elif user_num < num:
                print('Upper')
        print('You are out of guesses. Sorry!')
        return False
    return guess

# the_game = guess_num(55, 5)
# the_game()


low_lim_num = 1
up_lim_num = 100
min_tries = 1
max_tries = 10

def guess_decorator(function: callable) -> callable:
    @wraps(function)
    def wrap_game(num: int, tries: int) -> bool:
        if num < low_lim_num or num > up_lim_num:
            num = randint(low_lim_num, up_lim_num)
        if tries < min_tries or tries > max_tries:
            tries = randint(min_tries, max_tries)
        return function(num, tries)
    return wrap_game

def count_starts(num):
    count_lst = []

    def dcrtr(func: callable) -> callable:
        @wraps(func)
        def inner_func(*args, **kwargs):
            for _ in range(num):
                count_lst.append(func(*args, **kwargs))
            return count_lst
        return inner_func
    return dcrtr


def json_cache(func: callable) -> callable:
    try:
        with open(f"{func.__name__}.json", 'r') as log:
            data = json.load(log)
    except FileNotFoundError:
        with open(f"{func.__name__}.json", 'w') as log:
            data = []
            json.dump(data, log, indent=4)

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        temp_dict = {'args': args, 'kwargs': kwargs, 'result': func(*args, **kwargs)}
        data.append(temp_dict)
        with open(f"{func.__name__}.json", 'w') as log:
            json.dump(data, log, indent=4)

    return wrapper

@count_starts(3)
@json_cache
@guess_decorator
def guess_num_game(num: int, tries: int) -> bool:
    for _ in range(tries):
        user_num = int(input('Guess the number: '))
        if user_num == num:
            print('That is it. Good job!')
            return True
        elif user_num > num:
            print('Lower')
        elif user_num < num:
            print('Upper')
    print('You are out of guesses. Sorry!')
    return False



guess_num_game(10, 3)
