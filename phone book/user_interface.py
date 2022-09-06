"""User Interface"""
# методы  для ввода и изменения информации в справочнике


contact_list = []


def add_contact():
    """ Добавление в тел.книгу"""
    contact_dict = {

        'first_name': '',
        'second_name': '',
        'phone': '',
        'descriptor': '',
    }
    first_name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    descriptor = input('Введите описание: ')
    contact_dict['first_name'] = first_name
    contact_dict['second_name'] = second_name
    contact_dict['phone'] = phone
    contact_dict['descriptor'] = descriptor

    contact_list.append(contact_dict)
    return contact_list


# add_contact()
# print(contact_dict)


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
