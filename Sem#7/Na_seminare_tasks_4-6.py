from os import mkdir
from random import randint, choice

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def name_generator(start: int, stop: int):
    return ''.join([choice(choice([VOWELS, CONSONANTS])) for _ in range(randint(start, stop))]).capitalize()


def rand_files_gena(min_len_name: int = 6,
                    max_len_name: int = 30,
                    min_bytes: int = 256,
                    max_bytes: int = 4096,
                    files_count: int = 42,
                    extensions: list[str] = None,
                    path: str = 'for_task4'):
    for _ in range(files_count):
        extension = choice(extensions)
        filename = name_generator(min_len_name, max_len_name)
        try:
            write_to_file(path, filename, extension, min_bytes, max_bytes)
        except FileNotFoundError:
            mkdir(path)
            write_to_file(path, filename, extension, min_bytes, max_bytes)


def rand_files_format_gena(extensions: list[str],
                           num_files: int,
                           path: str = 'for_task4'):
    rand_files_gena(extensions=extensions, files_count=num_files, path = path)

def write_to_file(path, filename, extension, min_bytes, max_bytes):
    with open(f'{path}/{filename + extension}', 'w') as file:
        data = bytes(randint(1, 255) for _ in range(randint(min_bytes, max_bytes)))
        file.write(str(data))

rand_files_format_gena(
    extensions=['.txt', '.md', '.json', '.jpeg'],
    num_files=25)
