"""Запуск чат бота с телефонным справочником - точка входа"""
from aiogram import executor, types
from teleg_bot.create_bot import dp, my_command


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    """ Запуск бота с инлайн клавиатурой и выбором действия"""
    row_btns = [
        types.InlineKeyboardButton(
            text='Добавить контакт', callback_data=my_command.new(action='add_contact_in_book')),
        types.InlineKeyboardButton(
            text='Найти контакт', callback_data=my_command.new(action='find_contact')),
        types.InlineKeyboardButton(
            text='Изменить контакт', callback_data=my_command.new(action='changed_contact')),
        types.InlineKeyboardButton(
            text='Удалить контакт', callback_data=my_command.new(action='del_contact')),
        # types.InlineKeyboardButton(
        #     text='Показать всю книгу', callback_data=my_command.new(action='show_contact')),
    ]
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    keyboard_markup.add(*row_btns)

    await message.answer("PHONE BOOK", reply_markup=keyboard_markup)


# старт
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
