""" Handler для добавления контакта в телефонную книгу"""
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from teleg_bot.create_bot import dp, my_command


class FSMBase(StatesGroup):
    """Класс для временного хранилища информации"""
    first_name = State()
    second_name = State()
    phone_namber = State()
    description = State()


@dp.callback_query_handler(my_command.filter(action='add_contact_in_book'), state=None)
async def add_first_name(call: types.CallbackQuery):
    """ Добавление в тел.книгу"""
    await FSMBase.first_name.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('add_contact_in_book')
    await call.message.edit_text('Введите имя контакта')


@dp.message_handler(state=FSMBase.first_name)
async def add_second_name(message: types.Message, state: FSMContext):
    """ some func"""
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMBase.next()            # переключаемся на следующее состояние amount
    await message.answer('Введите фамилию')
    # добавить проверку на числовое значение этого поля
    await state.finish()
