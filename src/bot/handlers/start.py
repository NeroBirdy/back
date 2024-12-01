import json
from aiogram import types, Router
from aiogram.filters import Command

from src.bot.filters import filters
from src.auth import service as auth_service
from src.auth import schemas as auth_schemas
from src.bot.handlers.vks import keyboard as vks_keyboard

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message, WebAppData, KeyboardButton, ReplyKeyboardMarkup

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    button = KeyboardButton(text="Открыть WebApp", web_app=types.WebAppInfo(url="https://15bc-188-19-202-149.ngrok-free.app/login"))

    keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    await message.answer("Нажмите кнопку ниже для авторизации:", reply_markup=keyboard)


@router.message(filters.WebAppDataFilter())
async def webapp_data_handler(message: types.Message):
    if message.web_app_data:
        data = json.loads(message.web_app_data.data)
        print(data)
        user_data = auth_schemas.User(
            telegram_id = message.from_user.id,
            token = data
        )

        if await auth_service.UserService.get_by_telegram_id(telegram_id = message.from_user.id) == None :
            await auth_service.UserService.create(user_data=user_data)
        else:
            await auth_service.UserService.update(user_data=user_data)

        await message.answer("Вы успешно авторизовались!", reply_markup=vks_keyboard)

    else:
        await message.answer("Произошла ошибка при авторизации")
