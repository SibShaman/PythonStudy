"""Запуск бота"""
from aiogram import executor, types
from config import dp, my_command


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
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
