from aiogram import types, Router
from aiogram.filters import Command

from src.bot.filters import filters

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message, WebAppData, KeyboardButton, ReplyKeyboardMarkup

router = Router()

token = ""

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Создаем кнопку с WebApp
    button = KeyboardButton(text="Открыть WebApp", web_app=types.WebAppInfo(url="https://15bc-188-19-202-149.ngrok-free.app/login"))

    # Создаем клавиатуру с этой кнопкой
    keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    await message.answer("Нажмите кнопку ниже для авторизации:", reply_markup=keyboard)


@router.message(filters.WebAppDataFilter())
async def webapp_data_handler(message: types.Message):
    # Проверяем, содержит ли сообщение данные WebApp
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"Получены данные из WebApp: {data}")
    else:
        await message.answer("Нет данных от WebApp.")
