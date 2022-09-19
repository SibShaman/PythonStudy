"""Запуск чат бота с телефонным справочником"""
import os
import pathlib
import logging
from typing import Text
from dotenv import load_dotenv, dotenv_values
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData
from phone_book import add_contact_in_book

BASE_DIR = pathlib.Path(__file__).parent
ENV_FILE_PATH = BASE_DIR / '.env'
# config = None

if ENV_FILE_PATH.exists():
    load_dotenv(ENV_FILE_PATH)
    config = dotenv_values(ENV_FILE_PATH)

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

my_command = CallbackData('function')


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    """ Запуск бота с инлайн клавиатурой и выбором действия"""
    row_btns = [
        types.InlineKeyboardButton(
            text='Добавить контакт', callback_data=('add_contact_in_book')),
        types.InlineKeyboardButton(
            text='Найти контакт', callback_data=('find_contact')),
        types.InlineKeyboardButton(
            text='Изменить контакт', callback_data=('changed_contact')),
        types.InlineKeyboardButton(
            text='Удалить контакт', callback_data=('del_contact')),
        # types.InlineKeyboardButton(
        #     text='Показать всю книгу', callback_data=my_command.new(function='show_contact')),
    ]
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    keyboard_markup.add(*row_btns)

    await message.answer("PHONE BOOK", reply_markup=keyboard_markup)


@dp.callback_query_handler(text_contains='add_contact_in_book')
async def add_content(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Ты вернулся В главное меню. Жми опять кнопки",
                                parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
