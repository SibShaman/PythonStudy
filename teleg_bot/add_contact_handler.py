""" Handler для добавления контакта в телефонную книгу"""
from aiogram import types
from teleg_bot.create_bot import bot, dp


@dp.callback_query_handler(text_contains='add_contact_in_book')
async def add_content(call: types.CallbackQuery):
    """заглушка для метода, просто рабочая штука"""
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Ты вернулся В главное меню. Жми опять кнопки",
                                parse_mode='Markdown')
