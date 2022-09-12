from .manage import read_data
from .user_interface import find_contact


FILE_NAME = 'phone_book/phone_book.csv'


def search_contact():
    a = read_data(FILE_NAME)
    return find_contact(a)


def changed_contact():
    a = read_data(FILE_NAME)
