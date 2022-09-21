""" Handler для изменения контакта в телефонной книге (поиск по номеру телефона)"""
# import csv
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
# from main import start_handler
from teleg_bot.create_bot import dp, my_command


class FSMChangedContact(StatesGroup):
    """Класс для временного хранилища информации"""
    find_contact = State()
    first_name = State()
    second_name = State()
    phone = State()
    descriptor = State()


@dp.callback_query_handler(my_command.filter(action='changed_contact'), state=None)
async def changed_data(call: types.CallbackQuery):
    """Поиск данных в файле хранилища всего справочника - инициализация для изменения"""
    await FSMChangedContact.find_contact.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('changed_contact_contact')
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler(state=FSMChangedContact.find_contact)
async def parse_num_phone(message: types.Message, state: FSMContext):
    """Поиск данных в файле хранилища всего справочника"""
    pass
