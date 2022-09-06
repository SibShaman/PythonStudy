""" modul for send data in files,
        get data from files"""


import user_interface as ui
import views
import csv


file_name = 'phone_book.csv'


def write_data():
    """ Пишем в файл csv"""
    with open(file_name, 'w', newline='') as wf:
        fieldnames = ['id', 'first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        return writer


def read_data(file_name: str):
    """Читаем из файла csv"""
    with open(file_name, 'r', encoding='utf8') as rf:
        dataset = csv.reader(rf, delimiter=' ')
        for row in dataset:
            print(','.join(row))
