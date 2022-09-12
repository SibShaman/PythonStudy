"""User Interface"""
# методы  для ввода и изменения информации в справочнике


def add_contact():
    """ Добавление в тел.книгу"""
    add_list = []
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

    add_list.append(contact_dict)
    return add_list


def find_contact(find_list: list) -> list:
    """Поиск контакта в телефонной книге"""
    find_name = input('Введите имя кого вы хотите найти: ')
    find_phone = input('Введите номер телефона кого вы хотите найти: ')
    list_ = []
    for item in find_list:
        if item[0] == find_name and item[2] == find_phone:
            list_.append(item)
    if list_:
        return list_
    else:
        return 'Нет такого контакта, попробуйте еще'


def update_contact(update_list: list) -> list:
    """ Изменение контакта в тел.книге"""
    update_name = input('Введите имя кого вы хотите изменить: ')
    update_phone = input('Введите номер телефона кого вы хотите заменить: ')
    list_ = []
    for item in update_list:
        if item[0] == update_name and item[2] == update_phone:
            item[0] = input('Введите имя: ')
            item[1] = input('Введите фамилию: ')
            item[2] = input('Введите номер телефона: ')
            item[3] = input('Введите описание: ')
            list_.append(item)
        else:
            return item
    return list_


def del_contact():
    """ Удаление контакта из телефонной книги"""
    pass
