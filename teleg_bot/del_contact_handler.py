"""Удаление контакта из телефонной книги"""
import csv
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import start_handler
from phone_book.manage import changed_data
from teleg_bot.create_bot import dp, my_command


class FSMDelContact(StatesGroup):
    """Класс для временного хранилища информации"""
    first_step = State()


@dp.callback_query_handler(my_command.filter(action='del_contact'), state=None)
async def del_mydata(call: types.CallbackQuery):
    """Поиск данных в файле хранилища всего справочника - инициализация для удаления"""
    await FSMDelContact.first_step.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('del_contact')
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler(state=FSMDelContact.first_step)
async def del_num_phone(message: types.Message, state: FSMContext):
    """Поиск данных в файле хранилища всего справочника и удаление контакта"""
    one_list = []
    with open('test.csv', 'r', encoding='utf8', newline='') as read_file:
        reader = csv.DictReader(read_file, delimiter=' ')
        for item in reader:
            one_list.append(item)
    # дописать момент если пользователь пытается удалить несуществующий контакт
    two_list = []
    for item in one_list:
        if item['phone'] != message.text:
            two_list.append(item)
    changed_data(two_list, 'test.csv')
    await state.finish()

    await start_handler(message)  # - возврат в меню
