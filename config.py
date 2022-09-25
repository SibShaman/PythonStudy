"""Файл конфигурации бота, основные настройки"""
import os
import pathlib
import logging
from dotenv import load_dotenv, dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher


BASE_DIR = pathlib.Path(__file__).parent
ENV_FILE_PATH = BASE_DIR / '.env'

if ENV_FILE_PATH.exists():
    load_dotenv(ENV_FILE_PATH)
    config = dotenv_values(ENV_FILE_PATH)

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

my_command = CallbackData('function', 'action')
