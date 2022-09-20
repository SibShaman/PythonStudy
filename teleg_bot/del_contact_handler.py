"""Удаление контакта из телефонной книги"""
import csv
from aiogram import types
from main import start_handler
from teleg_bot.create_bot import dp, my_command


@dp.callback_query_handler(my_command.filter(action='del_contact'))
async def del_mydata(call: types.CallbackQuery):
    """Поиск данных в файле хранилища всего справочника - инициализация для удаления"""
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler()
async def del_num_phone(message: types.Message):
    """Поиск данных в файле хранилища всего справочника и удаление контакта"""
    # надо файл перезаписать, сейчас ничего не происходит
    with open('test.csv', 'w', encoding='utf8', newline='') as write_file:
        # reader = csv.DictReader(write_file, delimiter=' ')
        fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(
            write_file, fieldnames=fieldnames, delimiter=' ')
        writer.writeheader()
        # # for line in reader:
        # #     writer.writerow(line)
        # my_list = []
        # for item in reader:
        #     my_list.append(item)

        # for item in my_list:
        #     if item['phone'] == message.text:
        #         my_list.remove(item)
        # if my_list:
        #     await message.reply(my_list)
        # else:
        #     await message.reply('Нет такого контакта, попробуйте еще')

    await start_handler(message)  # - возврат в меню
