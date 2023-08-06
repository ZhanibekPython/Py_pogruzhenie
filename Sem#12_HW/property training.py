# class School:
#     __shared_attrs = {
#         1: 'One',
#         2: 'Two',
#         3: 'Three'
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__shared_attrs
#
# test1 = School()
# test2 = School()
# test2.start = 'September 1'

class Study:

    def __init__(self, name:str, year: int | float):
        self.__name = name
        self.__year = year

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def set_name(self, new_name):
        self.__name = new_name

    def set_year(self, new_year):
        self.__year = new_year

    hz = property()
    hz = hz.setter(set_name)
    hz = hz.getter(get_name)


a = Study('Joe Tribbiani', 1991)


print(a.hz)
