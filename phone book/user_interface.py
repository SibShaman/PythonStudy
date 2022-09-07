"""User Interface"""
# методы  для ввода и изменения информации в справочнике
import csv

contact_list = []
file_name = 'phone_book.csv'


def add_contact():
    """ Добавление в тел.книгу"""
    contact_dict = {

        'first_name': '',
        'second_name': '',
        'phone': '',
        'descriptor': '',
    }
    contact_dict['first_name'] = input('Введите имя: ')
    contact_dict['second_name'] = input('Введите фамилию: ')
    contact_dict['phone'] = input('Введите номер телефона: ')
    contact_dict['descriptor'] = input('Введите описание: ')

    contact_list.append(contact_dict)
    return contact_list


def find_contact():
    """Поиск контакта в телефонной книге"""
    find_name = input('Введите имя кого вы хотите найти: ')
    find_phone = input('Введите номер телефона кого вы хотите найти: ')
    with open(file_name, 'r', encoding='utf8') as find_file:
        reader = csv.DictReader(find_file, delimiter=' ', )
        first_name, second_name, phone, descriptor = reader.fieldnames
        for row in reader:
            if row[first_name] == find_name or row[phone] == find_phone:
                print(row[first_name], row[second_name],
                      row[phone], row[descriptor])
        # else:
        #     print('Нет такого контакта')


def update_contact():
    """ Изменение контакта в тел.книге"""
    pass


def del_contact():
    """ Удаление контакта из телефонной книги"""
    pass


def show_contacts():
    """Посмотреть всю тел.книгу"""
    pass
