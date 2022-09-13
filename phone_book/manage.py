""" modul for write data in files,
        read data from files"""
import os
import csv


def write_data(list_: list, file: str):
    """ Пишем в файл csv"""
    with open(file, 'r+', encoding='utf8', newline='') as write_file:
        fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(
            write_file, fieldnames=fieldnames, delimiter=' ')
        if not os.path.isfile(file):
            writer.writeheader()
        for line in list_:
            writer.writerow(line)


def read_data(file: str) -> list:
    """Чтение файла и с возвращением списка списков из каждой строки """
    with open(file, 'r', encoding='utf8') as read_file:
        # fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        reader = csv.DictReader(read_file, delimiter=' ')
        list_ = []
        for row in reader:
            list_.append(row)
        return list_


def show_data(file: str) -> str:
    """Читаем из файла csv и выводим в консоль все """
    with open(file, 'r', encoding='utf8') as read_file:
        reader = csv.reader(read_file, delimiter=' ')
        for row in reader:
            print(', '.join(row))
