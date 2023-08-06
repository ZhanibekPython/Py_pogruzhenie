from string import ascii_letters
from ClassExceptions import *


class Study:
    """Name decriptor and checker inside"""

    RUS_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
    RUS_LETTERS_UPPER = RUS_LETTERS.upper()

    @classmethod
    def check_full_name(cls, full_name):
        if type(full_name) is not str:
            raise WrongDataError('ФИО должно быть строкой')
        if len(full_name.split()) != 3:
            raise TypeError('Неверный формат ФИО')

        allowed_simbols = ascii_letters + cls.RUS_LETTERS + cls.RUS_LETTERS_UPPER
        for word in full_name.split():
            if len(word) <= 1:
                raise TypeError('Проверьте корректность заполнения ФИО')
            if len(word.strip(allowed_simbols)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')
            if word.istitle() is False:
                raise TypeError('ФИО должно начинаться с заглавной буквы')

    def __set_name__(self, owner, full_name):
        self.p_name = '_' + full_name

    def __get__(self, instance, owner):
        return getattr(instance, self.p_name)

    def __set__(self, instance, value):
        self.check_full_name(value)
        setattr(instance, self.p_name, value)


class School:
    """Возвращает успеваемость каждого отдельного студента"""

    full_name = Study()

    def __init__(self, full_name: str, subj: str, marks, tests):
        self._full_name = full_name
        self._subj = subj
        self._marks = marks
        self._tests = tests
        self.storage = {}
        self.scoring(subj=self._subj, marks=self._marks, tests=self._tests)
        self.average_points()

    def scoring(self, subj, marks, tests):
        if self._full_name not in self.storage:
            self.storage[self._full_name] = {subj: {'Marks': marks, "Tests": tests}}
        else:
            if subj not in self.storage[self._full_name]:
                self.storage[self._full_name][subj] = {'Marks': marks, "Tests": tests}
            else:
                self.storage[self._full_name][subj]['Marks'] += marks
                self.storage[self._full_name][subj]['Tests'] += tests

        return self.storage

    def average_points(self):
        all_marks = []
        all_tests = []
        for key, value in self.storage[self._full_name].items():
            for mark in value['Marks']:
                all_marks.append(mark)
            for test in value['Tests']:
                all_tests.append(test)
        average_marks = sum(all_marks) / len(all_marks)
        average_tests = sum(all_tests) / len(all_tests)
        return average_marks, average_tests

    def __call__(self, *args, **kwargs):
        return (f'{self.storage}, ср. бал по всем дисциплинам: {self.average_points()[0]}, '
                f'средний бал по тестам: {self.average_points()[1]}')

    def __str__(self):
        return (f'{self.storage}, ср. бал по всем дисциплинам: {self.average_points()[0]}, '
                f'средний бал по тестам: {self.average_points()[1]}')


Vanya = School("Ivanov Ivan Ivanovich", 'Math', (4, 3, 5, 4), (91, 86, 71, 96))
Vanya.scoring('Math', (2, 3, 4, 5), (70, 80, 90, 100))
Vanya.scoring("Fisics", (5, 5, 5, 5), (95, 96, 97, 97))
Vanya.scoring("Geography", (5, 5, 5, 5), (95, 96, 97, 97))
print(Vanya())
