""" Handler для поиска контакта в телефонной книге (по номеру телефона)"""
import csv
from aiogram import types
from main import start_handler
from teleg_bot.create_bot import dp, my_command


@dp.callback_query_handler(my_command.filter(action='find_contact'))
async def find_name(call: types.CallbackQuery):
    """ Добавление в тел.книгу"""
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler()
async def parse_num_phone(message: types.Message):
    """Поиск данных в файле хранилище всего справочника"""
    with open('test.csv', 'r', encoding='utf8') as read_file:
        reader = csv.DictReader(read_file, delimiter=' ')
        my_list = []
        for item in reader:
            if item['phone'] == message.text:
                my_list.append(item)
        if my_list:
            await message.reply(my_list)
        else:
            await message.reply('Нет такого контакта, попробуйте еще')

    await start_handler(message)  # - возврат в меню
