import logging
import os
from collections import namedtuple

DB = namedtuple('DB', ['cataloque_name', 'catalogue_flag', 'catalogue_parent'])
logging.basicConfig(filename='db_info_log.log', level=logging.INFO, format='%(asctime) - %(message)')


def logging_info(path):
    try:
        with os.scandir(path) as files:
            for file in files:
                if file.is_file():
                    catalogue_name = file.path.split()[0]
                else:
                    catalogue_name = file.name

                catalogue_flag = file.is_dir()

                catalogue_parent = path

                log_info = DB(cataloque_name=catalogue_name,
                              catalogue_flag=catalogue_flag,
                              catalogue_parent=catalogue_parent)

                logging.info(DB)

    except:
        print("Произошла ошибка")


if __name__ == '__main__':
    path = input('Введите путь для обработки: ')



print(logging_info(path))