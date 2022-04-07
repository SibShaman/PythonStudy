# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

import sys


if __name__ == '__main__':
    len_command = list(map(int, sys.argv[1:]))
    with open('bakery.csv', 'r' , encoding='utf8') as show_data:
        _temp = show_data.readlines()
        if len(len_command) == 2:
            for i in _temp[len_command[0] -1:len_command[1]]:
                print(i.strip())
        elif len(len_command) == 1:
            for i in _temp[len_command[0] -1:]:
                print(i.strip())
        else:
            for i in _temp:
                print(i.strip())


    exit()
