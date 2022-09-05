"""User Interface"""
# методы  для ввода и изменения информации в справочнике


contact_list = []


def add_contact():
    """ Добавление в тел.книгу"""
    first_name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    descriptor = input('Введите описание: ')
    contact_list.append(first_name)
    contact_list.append(second_name)
    contact_list.append(phone)
    contact_list.append(descriptor)
    return contact_list


def find_contact():
    """Поиск контакта в телефонной книге"""


def change_contact():
    """ Изменение контакта в тел.книге"""
    pass


def del_contact():
    """ Удаление контакта из телефонной книги"""
    pass


def show_contacts():
    """Посмотреть всю тел.книгу"""
    pass
