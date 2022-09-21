""" Handler для поиска контакта в телефонной книге (по номеру телефона)"""
import csv
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import start_handler
from teleg_bot.create_bot import dp, my_command


class FSMFindContact(StatesGroup):
    """Класс для временного хранилища информации"""
    first_step = State()


@dp.callback_query_handler(my_command.filter(action='find_contact'), state=None)
async def find_data(call: types.CallbackQuery):
    """Поиск данных в файле хранилища всего справочника - инициализация"""
    await FSMFindContact.first_step.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('del_contact')
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler(state=FSMFindContact.first_step)
async def parse_num_phone(message: types.Message, state: FSMContext):
    """Поиск данных в файле хранилища всего справочника"""
    with open('test.csv', 'r', encoding='utf8') as read_file:
        reader = csv.DictReader(read_file, delimiter=' ')
        my_list = []
        for item in reader:
            if item['phone'] == message.text:
                my_list.append(item)
        if my_list:
            await message.answer(f'вот контакт который вы искали {my_list}')
        else:
            await message.answer('Нет такого контакта, попробуйте еще')
    await state.finish()

    await start_handler(message)  # - возврат в меню
