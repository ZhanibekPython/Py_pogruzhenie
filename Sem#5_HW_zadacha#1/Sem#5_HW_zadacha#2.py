"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем
в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
(решение задачи "не в одну строку" есть на 4 семинаре(5 задача))"""


def bonus_payment_dict(name, salary, extra) -> dict:
    return {nam: (sal * float(ext.replace('%', '')) / 100) for nam, sal, ext in zip(name, salary, extra)}


names = ['Sasha', 'Masha', 'Dasha']
salaries = [1000, 1200, 1400]
extras = ['10.25', '15', '20']

print(bonus_payment_dict(names, salaries, extras))
