""" modul for write data in files,
        read data from files"""

import csv
import user_interface as ui
# import views


file_name = 'phone_book.csv'


def write_data():
    """ Пишем в файл csv"""
    with open(file_name, 'a', encoding='utf8', newline='') as write_file:
        fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(
            write_file, fieldnames=fieldnames, delimiter=' ')
        temp_ = ui.add_contact()
        for line in temp_:
            writer.writerow(line)


write_data()


# def read_data(file_name: str):
#     """Читаем из файла csv"""
#     with open(file_name, 'r', encoding='utf8') as read_file:
#         dataset = csv.reader(read_file, delimiter=' ')
#         for row in dataset:
#             print(','.join(row))
