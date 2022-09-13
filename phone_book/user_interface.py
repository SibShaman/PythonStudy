"""User Interface"""
# методы  для ввода и изменения информации в справочнике


def add_contact() -> list:
    """ Добавление в тел.книгу"""
    contact_dict = {
        'first_name': '',
        'second_name': '',
        'phone': '',
        'descriptor': '',
    }
    add_list = []
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

    for item in update_list:
        if item['first_name'] == update_name and item['phone'] == update_phone:
            update_list.remove(item)
            item['first_name'] = input('Введите имя: ')
            item['second_name'] = input('Введите фамилию: ')
            item['phone'] = input('Введите номер телефона: ')
            item['descriptor'] = input('Введите описание: ')
            update_list.append(item)
    return update_list


def del_contact():
    """ Удаление контакта из телефонной книги"""
    pass
