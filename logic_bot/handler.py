"""Основной хендлер, контроль за действиями пользователя"""
import logging
import typing
from aiogram import types

from main import get_keyboard
# from logic_bot import calc
from main import dp, my_command, likes, bot


@dp.callback_query_handler(my_command.filter(action=['complex', 'float']))
async def callback_vote_action(call: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """Логика бота при поступлении команды"""
    # await call.message.edit_text('Введите первое число')

    logging.info('Got this callback data: %r', callback_data)
    await call.answer()  # don't forget to answer callback query as soon as possible
    callback_data_action = callback_data['action']

    likes_count = likes.get(call.from_user.id, 0)

    if callback_data_action == 'complex':
        likes_count += 1
    else:
        likes_count -= 1

    # update amount of likes in storage
    likes[call.from_user.id] = likes_count

    await bot.edit_message_text(
        f'You voted {callback_data_action}! Now you have {likes_count} vote[s].',
        call.from_user.id,
        call.message.message_id,
        reply_markup=get_keyboard(dp),
    )
