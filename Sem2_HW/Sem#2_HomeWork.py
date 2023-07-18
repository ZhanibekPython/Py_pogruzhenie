DIV_HEX = 16
ZERO = 0


def num_16_system_convertion(num):
    """Программа переводит любое число в шестнадцатиричную систему"""
    conversion = ''
    while num > ZERO:
        conversion += str(num % DIV_HEX)
        num //= DIV_HEX
    return conversion[::-1]


print(num_16_system_convertion(123))

from fractions import Fraction


def fraction(a, b):
    """Программа получает две строки вида “a/b” - дробь с числителем и знаменателем
    и возвращает их сумма и проиведение"""
    return a + b, a * b


print(fraction(1 / 2, 1 / 3))
