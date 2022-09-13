"""User Interface"""
# методы  для ввода и изменения информации в справочнике


def add_in_book() -> list:
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


def find_in_book(find_list: list) -> list:
    """Поиск контакта в телефонной книге"""
    find_name = input('Введите имя кого вы хотите найти: ')
    find_phone = input('Введите номер телефона кого вы хотите найти: ')
    list_ = []
    for item in find_list:
        if item['first_name'] == find_name and item['phone'] == find_phone:
            list_.append(item)
    if list_:
        return list_
    else:
        return 'Нет такого контакта, попробуйте еще'


def update_in_book(update_list: list) -> list:
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


def del_in_book(del_list: list) -> list:
    """ Удаление контакта из телефонной книги"""
    del_name = input('Введите имя кого вы хотите удалить: ')
    del_phone = input('Введите номер телефона кого вы хотите удалить: ')

    for item in del_list:
        if item['first_name'] == del_name and item['phone'] == del_phone:
            del_list.remove(item)

    return del_list
