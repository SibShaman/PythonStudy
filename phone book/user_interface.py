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
    contact_dict['first_name'] = input('Введите имя: ')
    contact_dict['second_name'] = input('Введите фамилию: ')
    contact_dict['phone'] = input('Введите номер телефона: ')
    contact_dict['descriptor'] = input('Введите описание: ')

    contact_list.append(contact_dict)
    return contact_list


def find_contact():
    """Поиск контакта в телефонной книге"""
    pass


def change_contact():
    """ Изменение контакта в тел.книге"""
    pass


def del_contact():
    """ Удаление контакта из телефонной книги"""
    pass


def show_contacts():
    """Посмотреть всю тел.книгу"""
    pass
