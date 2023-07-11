from os import listdir, chdir, rename
from pathlib import Path


def get_files() -> list[str]:
    name = list(map(str, input('Через запятую введите названия файлов для '
                               'редактирования(переименования): ').split(',')))
    return name

def get_new_names():
    new_names = list(map(str, input('Через запятую введите новые названия '
                                    'для файлов: ').split(',')))
    return new_names

def get_adres() -> str:
    return input('Укажите абсолютный адрес папки с файлами: ')


def full_renamer():
    old = get_files()
    new_name = get_new_names()
    exts = input('Укажите желаемое расширение: ')
    #chdir(Path(get_adres()))
    list_files = listdir(Path(get_adres()))
    count = 1
    for i,v in enumerate(old):
        if v in listdir(Path.cwd()):
            try:
                rename(v, f'{v}_{new_name[i]}{count}{exts}')
                count += 1
            except FileNotFoundError:
                print(f'Что-то не так! Проверь еще раз свой факин код')
        else:
            print(f'Указанный файл {old[i]} не найден!')

full_renamer()