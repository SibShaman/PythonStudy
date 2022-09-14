""" module phone_book logic"""
from phone_book.user_interface import add_in_book, del_in_book, find_in_book, update_in_book
from .manage import changed_data, show_data, write_data
from .manage import read_data

FILE_NAME = 'phone_book/phone_book.csv'


def add_contact_in_book():
    """ Запись нового контакта"""
    temp = add_in_book()
    return write_data(temp, FILE_NAME)


def search_contact():
    """Поиск контакта"""
    temp = read_data(FILE_NAME)
    return find_in_book(temp)


def changed_contact():
    """Изменение контакта в телефонной книге"""
    temp_list = read_data(FILE_NAME)
    temp = update_in_book(temp_list)
    return changed_data(temp, FILE_NAME)


def remove_contact():
    """Удаление контакта из телефонной книги"""
    temp_list = read_data(FILE_NAME)
    temp = del_in_book(temp_list)
    return changed_data(temp, FILE_NAME)


def show_contact():
    """ Показать всю телефонную книгу"""
    return show_data(FILE_NAME)
