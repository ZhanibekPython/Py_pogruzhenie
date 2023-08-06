# def stripper(strip_thing: str = ' '):
#     def strip_it(text: str):
#         return text.strip(strip_thing)
#
#     return strip_it
#
# a = stripper()
# print(a('   arai altik tamina    '))

import time

def time_eval(func):
    def inside_func(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        result = start - end
        return res
    return inside_func

@time_eval
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a, b

print(get_fast_nod(5, 10))