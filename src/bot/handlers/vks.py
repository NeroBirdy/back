import asyncio
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F, Router
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import Message, WebAppData, KeyboardButton, ReplyKeyboardMarkup
from fastapi import requests
from httpx import AsyncClient

from src.auth import service as auth_service

router = Router()


button = KeyboardButton(text="Посмотреть созданные мной ВКС")
keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)


@router.message(F.text == "Посмотреть созданные мной ВКС")
async def cmd_view_my_meetings(message: Message):
    current_user = await auth_service.UserService.get_by_telegram_id(telegram_id=message.from_user.id)
    
    if current_user is None:
        await message.answer("Вы не авторизованы")
        return

    current_user_token = current_user.token.get("token")
    current_user_id = current_user.token.get("user")
    current_user_id = current_user_id.get("id")

    base_url = "https://test.vcc.uriit.ru/api/meetings"
    headers = {
        "Authorization": f"Bearer {current_user_token}",
        "accept": "application/json",
    }
    now = datetime.utcnow()

    days_since_monday = (now.weekday() - 0) % 7

    start_of_week = now - timedelta(days=days_since_monday)

    end_of_week = start_of_week + timedelta(days=6)

    params = {
        "fromDatetime": start_of_week.isoformat(),
        "toDatetime": end_of_week.isoformat(),
        "buildingId": current_user_id,
        "roomId": 1,
        "page": 1,
        "sort_by": "id",
    }

    try:
        async with AsyncClient() as client:
            response = await client.get(base_url, headers=headers, params=params)
        response.raise_for_status()

        response_data = response.json()
        meetings = response_data.get("data", [])
        
        if meetings:
            next_meeting = meetings[0]
            start_datetime = datetime.fromisoformat(next_meeting["startedAt"])
            formatted_datetime = start_datetime.strftime("%Y-%m-%d %H:%M:%S")
            meeting_info = (
                f"Ближайшее мероприятие:\n"
                f"Название: {next_meeting.get('name', 'Не указано')}\n"
                f"Дата начала: {formatted_datetime}\n"
                f"Ссылка: {next_meeting.get('permalink', 'Не указано')}\n"
            )
            await message.answer(meeting_info)
        else:
            await message.answer("Ближайшие мероприятия не найдены.")
    except Exception as err:
        print(f"Ошибка при запросе: {err}, Статус: {response.status_code}, Ответ: {response.text}")
        await message.answer("Произошла ошибка при обработке запроса.")

    
    


