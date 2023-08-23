# Задача 1

for i in range(2, 10):
    for j in range(2, 10):
        print(i, '*', j, '=', i * j, end='\t')
    print()

# попробовал через генератор (заколебался делать, но сделал)
print(''.join([''.join([f'{i} * {j} = {i * j}\t' for i in range(2, 10)]) + '\n' for j in range(2, 10)]))


# Задача 2 (В условии ничего не говорится про прямоугольные треугольники)
def triangle_solving(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print('Такого треугольника не бывает!')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    elif a != b != c:
        print('Треугольник разносторонний')
    return 'Треугольник равнобедренный'


triangle_solving(5, 5, 7)


# Задача 3

def num_check():
    num = int(input('Введите любое число, от 0 до 100К: '))
    check = len([i for i in range(1, num+1) if num % i == 0])
    return f'{num} - cоставное' if check > 2 else 'Простое'

print(num_check())

from random import randint
def guess_num():
    LOWER_LIMIT, UPPER_LIMIT = 0, 1000
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts = 10
    while num != (ask := int(input('Угадай число: '))):
        print('Больше' if ask < num else 'Меньше')
        attempts -= 1
        if ask == num:
            return 'Молодец! Угадал!'
        elif attempts == 0:
            return 'Сегодня не твой день!'

print(guess_num())