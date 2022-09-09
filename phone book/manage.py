""" modul for write data in files,
        read data from files"""
import os
import csv
import user_interface as ui
# import views


FILE_NAME = 'phone_book.csv'
file_exists = os.path.isfile(FILE_NAME)


def write_data(list_: list, file: str):
    """ Пишем в файл csv"""
    with open(file, 'a', encoding='utf8', newline='') as write_file:
        fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(
            write_file, fieldnames=fieldnames, delimiter=' ')
        if not file_exists:
            writer.writeheader()
        for line in list_:
            writer.writerow(line)


def read_data(file: str) -> list:
    """Чтение файла и с возвращением списка списков из каждой строки """
    with open(file, 'r', encoding='utf8') as read_file:
        reader = csv.reader(read_file, delimiter=' ')
        temp_list = []
        for row in reader:
            temp_list.append(row)
        return temp_list


def show_data(file: str) -> str:
    """Читаем из файла csv и выводим в консоль все """
    with open(file, 'r', encoding='utf8') as read_file:
        reader = csv.reader(read_file, delimiter=' ')
        for row in reader:
            print(', '.join(row))


write_data(ui.contact_list, FILE_NAME)
# print(read_data(FILE_NAME))
