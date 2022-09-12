""" module phone_book logic"""
from .manage import read_data
from .user_interface import find_contact


FILE_NAME = 'phone_book/phone_book.csv'


def search_contact():
    """Поиск контакта"""
    temp = read_data(FILE_NAME)
    return find_contact(temp)


def changed_contact():
    """Изменение контакта"""
    temp = read_data(FILE_NAME)
    # пока ничего не изменяет, надо вписать функцию по изменению и перезаписи всего файла
    return temp
