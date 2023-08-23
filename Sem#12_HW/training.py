from string import ascii_letters


class Study:
    RUS_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
    RUS_LETTERS_UPPER = RUS_LETTERS.upper()

    @classmethod
    def check_full_name(cls, full_name):

        if type(full_name) is not str:
            raise TypeError('ФИО должно быть строкой')

        if len(full_name.split()) != 3:
            raise TypeError('Неверный формат ФИО')

        allowed_simbols = ascii_letters + cls.RUS_LETTERS + cls.RUS_LETTERS_UPPER
        for word in full_name.split():
            if len(word) <= 1:
                raise TypeError('Проверьте корректность заполнения ФИО')
            if len(word.strip(allowed_simbols)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')
            if word.istitle() is not True:
                raise TypeError('ФИО должно начинаться с заглавной буквы')

    @classmethod
    def check_marks(cls, marks):
        if type(marks) != tuple:
            raise TypeError('Вам следует передевать оценки в кортеже')

        for digit in marks:
            if type(digit) != int:
                raise TypeError('Оценки должны быть целым числом')
            if 0 <= digit < 6 != True:
                raise TypeError('Оценки должны быть в диапозоне [0-5]')

    @classmethod
    def check_tests(cls, tests):
        if type(tests) != tuple:
            raise TypeError('Вам следует передевать результаты тестов в кортеже')

        for digit in tests:
            if type(digit) != int:
                raise TypeError('Результаты тестов должны быть целым числом')
            if 0 <= digit < 101 != True:
                raise TypeError('Результаты тестов должны быть в диапозоне [0-100]')

    def __set_name__(self, owner, name):
        self.p_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.p_name)

    def __set__(self, instance, full_name, marks, tests):
        self.check_full_name(full_name)
        self.check_marks(marks)
        self.check_tests(tests)
        setattr(instance, self.p_name, full_name)


class Student:
    __common_subjects = {
        'Math': [],
        'Chemistry': [],
        'Fisics': [],
        'Geography': []
    }

    full_name = Study()
    subject = Study()
    marks = Study()
    tests = Study()

    def __init__(self, full_name: str, subject: str, marks, tests):
        self.name = full_name
        self.subj = subject
        self.marks = marks
        self.tests = tests
        self.__dict__ = self.__common_subjects

    def __str__(self):
        return f'{self.full_name:} {self.subject} - Оценки: {self.marks}, результаты тестов: {self.tests}'

stud1 = Student('Ivanov Ivan Ivanovich', 'Math', (4, 5, 4, 5), (95, 88, 74, 91))

print(stud1.__dict__)
