""" Handler для изменения контакта в телефонной книге (поиск по номеру телефона)"""
# import csv
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from phone_book.manage import changed_data, read_data
from main import start_handler
from teleg_bot.create_bot import dp, my_command


class FSMChangedContact(StatesGroup):
    """Класс для временного хранилища информации"""
    find_step = State()
    first_name = State()
    second_name = State()
    phone = State()
    descriptor = State()


@dp.callback_query_handler(my_command.filter(action='changed_contact'), state=None)
async def changed_contact(call: types.CallbackQuery):
    """Поиск данных в файле хранилища всего справочника - инициализация для изменения"""
    await FSMChangedContact.find_step.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('changed_contact_contact')
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler(state=FSMChangedContact.find_step)
async def find_del_contact(message: types.Message, state: FSMContext):
    """Поиск данных в файле хранилища всего справочника"""
    async with state.proxy() as data:
        data['find_step'] = message.text

    one_list = read_data('test.csv')
    two_list = []
    for item in one_list:
        if item['phone'] != message.text:
            two_list.append(item)
    changed_data(two_list, 'test.csv')

    await FSMChangedContact.next()
    await message.answer('Введите имя контакта')


@dp.message_handler(state=FSMChangedContact.first_name)
async def changed_first_name(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим имя и переключаемся на следующее состояние"""
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMChangedContact.next()
    await message.answer('Введите фамилию')


@dp.message_handler(state=FSMChangedContact.second_name)
async def changed_second_name(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим фамилию и переключаемся на следующее состояние"""
    async with state.proxy() as data:
        data['second_name'] = message.text
    # переключаемся на следующее состояние phone_namber
    await FSMChangedContact.next()
    await message.answer('Введите номер телефона')


@dp.message_handler(state=FSMChangedContact.phone)
async def changed_phone_namber(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим номер телефона и переключаемся на следующее состояние"""
    async with state.proxy() as data:
        data['phone'] = message.text
    # переключаемся на следующее состояние phone_namber
    await FSMChangedContact.next()
    await message.answer('Введите описание контакта')


@dp.message_handler(state=FSMChangedContact.descriptor)
async def changed_description(message: types.Message, state: FSMContext):
    """ Добавление в тел.книгу - вводим описание и выходим из машины состояний"""
    async with state.proxy() as data:
        data['descriptor'] = message.text
    my_dict = await state.get_data()
    del my_dict['find_step']
    print(my_dict)
    changed_list = read_data('test.csv')
    changed_list.append(my_dict)
    changed_data(changed_list, 'test.csv')

    await state.finish()

    await start_handler(message)  # - возврат в меню
