import csv
from aiogram import types
from main import start_handler
from teleg_bot.create_bot import dp, my_command


@dp.callback_query_handler(my_command.filter(action='changed_contact'))
async def changed_data(call: types.CallbackQuery):
    """Поиск данных в файле хранилища всего справочника - инициализация для изменения"""
    await call.message.edit_text('Введите номер телефона')


@dp.message_handler()
async def parse_num_phone(message: types.Message):
    """Поиск данных в файле хранилища всего справочника и замена на релевантное значение"""
    await start_handler(message)  # - возврат в меню
