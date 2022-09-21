""" Handler для просмотра всей телефонной книги (скачивание csv)"""
from aiogram import types
from teleg_bot.create_bot import dp, my_command


@dp.callback_query_handler(my_command.filter(action='show_contact'))
async def del_mydata(call: types.CallbackQuery):
    """Скачивание бинарного файла в котором хранится вся база данных нашего справочника"""
    await call.message.reply_document(
        open('C:\\Users\\USER\\PythonProjects\\PythonStudy\\test.csv', 'rb'))
