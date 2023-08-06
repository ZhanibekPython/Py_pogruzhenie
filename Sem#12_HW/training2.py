class Proverka:
    """Proveryayu public, protected and private atrrs"""

    def __init__(self, a, b):
        if self.__another_check(a) and self.__another_check(b):
            self.__a = a
            self.__b = b


    @classmethod
    def __another_check(cls, arg):
        return type(arg) in (int, float)

    def set_val(self, a, b):
        if self.__another_check(a) and self.__another_check(b):
            self.__a = a
            self.__b = b
        else:
            raise ValueError("A ne powel by ty nahui")

    def geting(self):
        return self.__a, self.__b


test = Proverka(10, 20)
test.set_val(50, 55)
print(test.geting())

