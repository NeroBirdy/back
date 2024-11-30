import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message, WebAppData, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage

from src.settings import settings
from src.bot.handlers import register_routes

from src.bot.filters import filters

bot = Bot(token=settings.telegram_bot.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Создаем кнопку с WebApp
    button = KeyboardButton(text="Открыть WebApp", web_app=types.WebAppInfo(url="https://d62d-188-19-202-149.ngrok-free.app"))

    # Создаем клавиатуру с этой кнопкой
    keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    await message.answer("Нажмите кнопку ниже для авторизации:", reply_markup=keyboard)


@dp.message(filters.WebAppDataFilter())
async def webapp_data_handler(message: types.Message):
    # Проверяем, содержит ли сообщение данные WebApp
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"Получены данные из WebApp: {data}")
    else:
        await message.answer("Нет данных от WebApp.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

async def start_bot():
    try:
        await bot.send_message(settings.telegram_bot.ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(settings.telegram_bot.ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass