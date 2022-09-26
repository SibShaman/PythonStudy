"""Файл конфигурации бота, основные настройки, запуск бота"""
import os
import pathlib
import logging
from dotenv import load_dotenv, dotenv_values
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, executor, types


BASE_DIR = pathlib.Path(__file__).parent
ENV_FILE_PATH = BASE_DIR / '.env'

if ENV_FILE_PATH.exists():
    load_dotenv(ENV_FILE_PATH)
    config = dotenv_values(ENV_FILE_PATH)

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)


dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

my_command = CallbackData('function', 'action')

likes = {}


@dp.message_handler(commands='start')
async def get_keyboard(message: types.Message):
    """ Запуск бота с инлайн клавиатурой и выбором действия"""
    row_btns = [
        types.InlineKeyboardButton(
            text='Комплексные числа', callback_data=my_command.new(action='complex')),
        types.InlineKeyboardButton(
            text='Вещественные числа', callback_data=my_command.new(action='float')),
    ]
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    keyboard_markup.add(*row_btns)

    await message.answer(
        "Калькулятор вещественных и комплексных чисел", reply_markup=keyboard_markup)


# старт
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
