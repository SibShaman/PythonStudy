"""Запуск чат бота с телефонным справочником"""
import os
import pathlib
import logging
from dotenv import load_dotenv, dotenv_values
from aiogram import Bot, Dispatcher, executor, types


BASE_DIR = pathlib.Path(__file__).parent
ENV_FILE_PATH = BASE_DIR / '.env'
# config = None

if ENV_FILE_PATH.exists():
    load_dotenv(ENV_FILE_PATH)
    config = dotenv_values(ENV_FILE_PATH)

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):

    row_btns = [
        types.InlineKeyboardButton(
            text='Добавить контакт', callback_data='add_contact'),
        types.InlineKeyboardButton(
            text='Найти контакт', callback_data='find_contact'),
        types.InlineKeyboardButton(
            text='Изменить контакт', callback_data='changed_contact'),
        types.InlineKeyboardButton(
            text='Удалить контакт', callback_data='del_contact'),
        types.InlineKeyboardButton(
            text='Показать всю книгу', callback_data='show_contact'),
    ]
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    keyboard_markup.add(*row_btns)

    await message.answer("PHONE BOOK", reply_markup=keyboard_markup)


# Use multiple registrators. Handler will execute when one of the filters is OK
# @dp.callback_query_handler(text='no')  # if cb.data == 'no'
# @dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
# async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
#     answer_data = query.data
#     # always answer callback queries, even if you have nothing to say
#     await query.answer(f'You answered with {answer_data!r}')

#     if answer_data == 'yes':
#         text = 'Great, me too!'
#     elif answer_data == 'no':
#         text = 'Oh no...Why so?'
#     else:
#         text = f'Unexpected callback data {answer_data!r}!'

#     await bot.send_message(query.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
