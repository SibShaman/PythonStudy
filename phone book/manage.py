""" modul for write data in files,
        read data from files"""
import os
import csv
import user_interface as ui
# import views


file_name = 'phone_book.csv'
file_exists = os.path.isfile(file_name)


def write_data():
    """ Пишем в файл csv"""
    with open(file_name, 'a', encoding='utf8', newline='') as write_file:
        fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(
            write_file, fieldnames=fieldnames, delimiter=' ')
        if not file_exists:
            writer.writeheader()
        for line in ui.contact_list:
            writer.writerow(line)


ui.update_contact()
# ui.add_contact()
# write_data()
# ui.find_contact()


def read_data():
    """Читаем из файла csv"""
    with open(file_name, 'r', encoding='utf8') as read_file:
        dataset = csv.reader(read_file, delimiter=' ')
        for row in dataset:
            print(', '.join(row))


# read_data()
