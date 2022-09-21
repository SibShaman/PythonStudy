""" Handler для поиска контакта в телефонной книге (по номеру телефона)"""
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import start_handler
from phone_book.manage import read_data
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

    one_list = read_data('test.csv')
    two_list = []
    for item in one_list:
        if item['phone'] == message.text:
            two_list.append(item)
    if two_list:
        await message.answer(f'вот контакт который вы искали {two_list}')
    else:
        await message.answer('Нет такого контакта, попробуйте еще')

    await state.finish()

    await start_handler(message)  # - возврат в меню
