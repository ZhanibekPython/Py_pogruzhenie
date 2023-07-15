from sys import argv


__all__ = ['zagad', 'mnogo_zagad', 'create_counter_dict', 'show_counter_dict', '']


_tries_dict = {}


def zagad(text: str, ans_list: list[str], tries: int = 3) -> int:
    """Получаем загадку, список с возможными отгадок
    и кол-во попыток на угадывание. Возвращает номер попытки
    с которой была одгадана загадка
    или ноль если попытки исчерпаны"""
    print(text)
    count = 0
    ans_list = list(map(lambda x: x.lower(), ans_list))
    while tries > count:
        count += 1
        if input('Ответ на загадку: ').lower() in ans_list:
            return count
    return 0


def mnogo_zagad():
    ZAGADKI = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
    }

    for key, value in ZAGADKI.items():
        create_counter_dict(key, zagad(key, value))


def create_counter_dict(text: str, tries: int):
    """Подсчет попыток"""
    _tries_dict[text] = tries


def show_counter_dict():
    """Просмотр попыток"""
    print('-' * 10, 'Ваши попытки', '-' * 10)
    for k, v in _tries_dict.items():
        print(k, v)


if __name__ == '__main__':
    mnogo_zagad()
    show_counter_dict()
