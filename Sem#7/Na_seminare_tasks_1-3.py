# # task_1
from random import randint, choice


def isfile_full(length: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(length):
            random_num = randint(-1000, 1000)
            random_num2 = float(f'{randint(-1000, 1000)}.{randint(0, 1000)}')
            file.write(f'{random_num} and {random_num2}\n')


# task_2

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def full_of_names(length: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as names:
        for _ in range(length):
            print(name_generator() + '\n', file=names, end='')


def name_generator(start: int, stop: int):
    return ''.join([choice(choice([VOWELS, CONSONANTS])) for i in range(randint(4, 7))]).capitalize()


# task_3
def finalization(names_filename: str, nums_filename: str, final_filename: str):
    isfile_full(randint(10, 20), nums_filename)
    full_of_names(randint(10, 20), names_filename)

    with open(nums_filename) as nums_file:
        num = nums_file.read().split('\n')[:-1]

    with open(names_filename) as names_file:
        name = names_file.read().split('\n')[:-1]

    nums_list_len = len(num)
    names_list_len = len(name)

    if nums_list_len > names_list_len:
        name = name + name[:nums_list_len - names_list_len]
    else:
        num = num + num[:names_list_len - nums_list_len]

    num = list(map(lambda x: (int(x.split(' and ')[0]), float(x.split(' and ')[1])), num))

    with open(final_filename, 'w') as result_file:
        for names, nums in zip(name, num):
            result_mult = nums[0] * nums[1]
            if result_mult > 0:
                result_name = names.upper()
                result_mult = int(result_mult)
            else:
                result_name = names.lower()
                result_mult = result_mult * -1

            result_file.write(f"{result_name} {result_mult}\n")


finalization('Numbers', 'Namesss', 'Done')