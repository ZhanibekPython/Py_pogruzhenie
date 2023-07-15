from sys import argv


def check_date(date: str) -> bool:
    dd, mm, yy = map(int, date.split('.'))
    if 0 < dd <= 31 and 0 <= mm <=12 and 1 <=yy <10000:
        return True
    return False



def _vis_yy(date: str) -> bool:
    dd, mm, yy = map(int, date.split('.'))
    if yy % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    print(check_date('05.06.1998'))
    print(_vis_yy('05.06.1998'))