from datetime import datetime
import logging
import argparse

logging.basicConfig(filename="date_log", level=logging.ERROR, encoding="utf-8")

WEEKDAYS = ("", "понедельник", "вторник", "среда", "четверг",
            "пятница", "суббота", "воскресенье")

MONTHS = ("", "января", "февраля", "марта", "апреля",
          "мая", "июня", "июля", "августа", "сентября",
          "октября", "ноября", "декабря")



def text(text: str):
    try:
        week_count, weekday, month = text.split()
        week_count = int(week_count[0])
        weekday = WEEKDAYS.index(weekday)
        month = MONTHS.index(month)
        count = 0
        for date in range(1, 32):
            temp_date = datetime(day=date, month=month, year=datetime.now().year)
            if temp_date.weekday == weekday:
                count += 1
                if count == week_count:
                    return temp_date
        else:
            return None
    except ValueError:
        logging.error(f'Неверный формат данных {text}')
        return None

def parse():
    parser = argparse.ArgumentParser(prog=text)
    parser.add_argument()



if __name__ == "__main__":
    print(text('3-й четверг ноября'))


