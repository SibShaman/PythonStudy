from .manage import read_data
from .user_interface import find_contact


FILE_NAME = 'phone_book.csv'

def some_func():
    a = read_data(FILE_NAME)
    return find_contact(a)
