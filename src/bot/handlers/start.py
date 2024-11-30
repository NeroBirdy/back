import json
from aiogram import types, Router
from aiogram.filters import Command

from src.bot.filters import filters
from src.auth import service as auth_service
from src.auth import schemas as auth_schemas

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message, WebAppData, KeyboardButton, ReplyKeyboardMarkup

router = Router()


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
        data = json.loads(message.web_app_data.data)

        user_data = auth_schemas.UserCreateDB(
            telegram_id = message.from_user.id,
            token = data
        )
        await auth_service.UserService.create(user_data=user_data)
    else:
        await message.answer("Нет данных от WebApp.")
