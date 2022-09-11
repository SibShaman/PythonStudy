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


def update_contact(read_list: list) -> list:
    """ Изменение контакта в тел.книге"""
    update_name = input('Введите имя кого вы хотите изменить: ')
    update_phone = input('Введите номер телефона кого вы хотите заменить: ')





    # with open(file_name, 'r+', encoding='utf8') as find_file:
    #     reader = csv.DictReader(find_file, delimiter=' ', )
    #     first_name, second_name, phone, descriptor = reader.fieldnames

    #     fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
    #     writer = csv.DictWriter(
    #         find_file, fieldnames=fieldnames, delimiter=' ')

    #     for row in reader:
    #         if row[first_name] == update_name or row[phone] == update_phone:
    #             row['first_name'] = input('Введите имя: ')
    #             row['second_name'] = input('Введите фамилию: ')
    #             row['phone'] = input('Введите номер телефона: ')
    #             row['descriptor'] = input('Введите описание: ')


def del_contact():
    """ Удаление контакта из телефонной книги"""
    pass
