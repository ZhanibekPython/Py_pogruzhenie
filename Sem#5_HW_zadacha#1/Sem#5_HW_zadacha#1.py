""" Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt') """

def absolute_path_partitition(adres: str):
    path = adres[:adres.rfind('/')]
    format = '.' + adres.split('.')[-1]
    name = adres.split('/')[-1].split('.')[0]
    return path, name, format

print(absolute_path_partitition('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'))