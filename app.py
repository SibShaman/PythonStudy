""" Phone Book"""
# точка входа в приложение
from phone_book import add_contact_in_book, changed_contact
from phone_book import remove_contact, search_contact, show_contact
from phone_book import send_json_one, send_json_two


while True:
    print('Телефонный справочник')
    print('Меню')
    print('1. Добавить контакт в телефонную книгу ')
    print('2. Найти контакт в телефонной книге ')
    print('3. Изменить контакт ')
    print('4. Удалить контакт ')
    print('5. Показать всю телефонную книгу ')
    print('6. Отправить в JSON (структура файла №1)')
    print('7. Отправить в JSON (структура файла №2)')
    print('0. Выход')

    marker = input('Введите номер: ')

    if marker == '1':
        add_contact_in_book()
    elif marker == '2':
        print(search_contact())
    elif marker == '3':
        changed_contact()
    elif marker == '4':
        remove_contact()
    elif marker == '5':
        show_contact()
    elif marker == '6':
        send_json_one()
    elif marker == '7':
        send_json_two()
    elif marker == '0':
        print('Досвидания')
        break
    else:
        print('Вы не правильно сделали выбор, попробуйте еще раз')
        break
