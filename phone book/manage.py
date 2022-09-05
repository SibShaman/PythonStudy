""" modul for send data in files,
        get data from files"""

import user_interface as ui
import views


def send_data():
    ui.add_contact()
    with open('phone_book.txt', 'a', encoding='utf8') as file:
        file.write(f"{' '.join(ui.contact_list)}\n")


def get_data():
    pass


# print(send_data())
send_data()
