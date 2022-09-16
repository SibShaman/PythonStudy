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
