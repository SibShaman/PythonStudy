""" Handler для добавления контакта в телефонную книгу"""
import os
import csv
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import start_handler
from teleg_bot.create_bot import dp, my_command


class FSMAddContact(StatesGroup):
    """Класс для временного хранилища информации"""
    first_name = State()
    second_name = State()
    phone = State()
    descriptor = State()


@dp.callback_query_handler(my_command.filter(action='add_contact_in_book'), state=None)
async def initial_state(call: types.CallbackQuery):
    """ Добавление в тел.книгу - начальное состояние"""
    await FSMAddContact.first_name.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('add_contact_in_book')
    await call.message.edit_text('Введите имя контакта')


@dp.message_handler(state=FSMAddContact.first_name)
async def add_first_name(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим имя и переключаемся на следующее состояние"""
    async with state.proxy() as data:
        data['first_name'] = message.text
    # переключаемся на следующее состояние second_name
    await FSMAddContact.next()
    await message.answer('Введите фамилию')


@dp.message_handler(state=FSMAddContact.second_name)
async def add_second_name(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим фамилию и переключаемся на следующее состояние"""
    async with state.proxy() as data:
        data['second_name'] = message.text
    # переключаемся на следующее состояние phone_namber
    await FSMAddContact.next()
    await message.answer('Введите номер телефона')


@dp.message_handler(state=FSMAddContact.phone)
async def add_phone_namber(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим номер телефона и переключаемся на следующее состояние"""
    async with state.proxy() as data:
        data['phone'] = message.text
    # переключаемся на следующее состояние phone_namber
    await FSMAddContact.next()
    await message.answer('Введите описание контакта')


@dp.message_handler(state=FSMAddContact. descriptor)
async def add_description(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим описание и выходим из машины состояний"""
    async with state.proxy() as data:
        data['descriptor'] = message.text

    my_dict = await state.get_data()  # сохраняем из машины состояний данные
    # и записываем данные
    file_exists = os.path.isfile('test.csv')
    with open('test.csv', 'a+', encoding='utf8') as write_file:
        fieldnames = ['first_name', 'second_name', 'phone', 'descriptor']
        writer = csv.DictWriter(
            write_file, fieldnames=fieldnames, delimiter=' ', lineterminator='\n')
        if not file_exists:
            writer.writeheader()
        writer.writerow(my_dict)

    await state.finish()
    await start_handler(message)  # - возврат в меню
