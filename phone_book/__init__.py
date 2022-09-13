""" module phone_book logic"""
from .manage import write_data
from .manage import read_data
from .user_interface import add_contact, find_contact, update_contact


FILE_NAME = 'phone_book/phone_book.csv'


def search_contact():
    """Поиск контакта"""
    temp = read_data(FILE_NAME)
    return find_contact(temp)


def changed_contact():
    """Изменение контакта"""
    temp_list = read_data(FILE_NAME)
    temp = update_contact(temp_list)
    # пока ничего не изменяет, надо вписать функцию по изменению и перезаписи всего файла
    return write_data(temp, FILE_NAME)


def add_contact_in_book():
    """ Запись нового контакта"""
    temp = add_contact()
    return write_data(temp, FILE_NAME)
