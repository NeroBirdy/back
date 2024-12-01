import asyncio
from datetime import datetime, timedelta
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, FSInputFile
from aiogram import Router, F
from httpx import AsyncClient
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from src.auth import service as auth_service

router = Router()

# Клавиатура
button1 = KeyboardButton(text="Еженедельник на эту неделю")
button2 = KeyboardButton(text="Еженедельник на следующую неделю")
keyboard = ReplyKeyboardMarkup(keyboard=[[button1],[button2]], resize_keyboard=True)

@router.message(F.text == "Еженедельник на эту неделю")
async def cmd_view_my_meetings(message: Message):
    current_user = await auth_service.UserService.get_by_telegram_id(telegram_id=message.from_user.id)

    if current_user is None:
        await message.answer("Вы не авторизованы")
        return

    current_user_token = current_user.token.get("token")
    base_url = "https://test.vcc.uriit.ru/api/meetings"
    headers = {
        "Authorization": f"Bearer {current_user_token}",
        "accept": "application/json",
    }
    now = datetime.utcnow()

    # Определение начала и конца недели
    start_of_week = now - timedelta(days=now.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    params = {
        "fromDatetime": start_of_week.isoformat(),
        "toDatetime": end_of_week.isoformat(),
        "buildingId": 2,
        "sort_by": "id",
    }

    try:
        async with AsyncClient() as client:
            response = await client.get(base_url, headers=headers, params=params)
            response.raise_for_status()

        response_data = response.json()
        meetings = response_data.get("data", [])

        if meetings:
            events = {
                meeting["id"]: {
                    "start": datetime.fromisoformat(meeting["startedAt"]),
                    "end": datetime.fromisoformat(meeting["endedAt"]),
                    "text": meeting.get("name", "Не указано")
                }
                for meeting in meetings
            }

            # Создание изображения расписания
            image = await create_calendar_image(start_of_week, end_of_week, events)
            with open("schedule.png", "wb") as f:
                f.write(image.read())

            input_file = FSInputFile("schedule.png")
            await message.answer_photo(input_file, caption="Ваш еженедельник на эту неделю")
        else:
            await message.answer("На этой неделе нет мероприятий.")

    except Exception as err:
        await message.answer(f"Произошла ошибка")


@router.message(F.text == "Еженедельник на следующую неделю")
async def cmd_view_my_meetings(message: Message):
    current_user = await auth_service.UserService.get_by_telegram_id(telegram_id=message.from_user.id)

    if current_user is None:
        await message.answer("Вы не авторизованы")
        return

    current_user_token = current_user.token.get("token")
    base_url = "https://test.vcc.uriit.ru/api/meetings"
    headers = {
        "Authorization": f"Bearer {current_user_token}",
        "accept": "application/json",
    }
    now = datetime.utcnow()

    # Определение начала и конца недели
    start_of_week = now - timedelta(days=now.weekday()) + timedelta(days=7)
    end_of_week = start_of_week + timedelta(days=6) + timedelta(days=7)

    params = {
        "fromDatetime": start_of_week.isoformat(),
        "toDatetime": end_of_week.isoformat(),
        "buildingId": 2,
        "sort_by": "id",
    }

    try:
        async with AsyncClient() as client:
            response = await client.get(base_url, headers=headers, params=params)
            response.raise_for_status()

        response_data = response.json()
        meetings = response_data.get("data", [])

        if meetings:
            events = {
                meeting["id"]: {
                    "start": datetime.fromisoformat(meeting["startedAt"]),
                    "end": datetime.fromisoformat(meeting["endedAt"]),
                    "text": meeting.get("name", "Не указано")
                }
                for meeting in meetings
            }

            image = await create_calendar_image(start_of_week, end_of_week, events)
            with open("schedule.png", "wb") as f:
                f.write(image.read())

            input_file = FSInputFile("schedule.png")
            await message.answer_photo(input_file, caption="Ваш еженедельник на следующую неделю")
        else:
            await message.answer("На следующей неделе нет мероприятий")

    except Exception as err:
        await message.answer(f"Произошла ошибка")


async def create_calendar_image(start_of_week, end_of_week, events):
    width, height = 743, 402
    image = Image.new("RGB", (width, height), (217, 235, 255))
    draw = ImageDraw.Draw(image)

    # Шрифты
    font_path = 'src/bot/handlers/ofont.ru_Hero.ttf'
    font = ImageFont.truetype(font_path, 12)
    font_title = ImageFont.truetype(font_path, 16)
    font_events = ImageFont.truetype(font_path, 10)
    font_date = ImageFont.truetype(font_path, 8)

    # Заголовок
    draw.text((width // 2 - 50, 15), "Еженедельник", font=font_title, fill=(0, 0, 0))

    # Таблица
    table_start_y = 50
    column_width = width // 19
    row_height = height // 9

    for i in range(1, 19):
        draw.line((i * column_width, table_start_y, i * column_width, table_start_y + 8 * row_height), fill=(0, 0, 0), width=2)

    for i in range(0, 9):
        draw.line((0, table_start_y + i * row_height, width, table_start_y + i * row_height), fill=(0, 0, 0), width=2)

    # Дни недели
    days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    current_date = start_of_week

    for i, day in enumerate(days_of_week):
        # Рисуем день недели
        bbox = draw.textbbox((0, 0), day, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw.text(
            ((column_width - text_width) // 2, table_start_y + (i + 1) * row_height + (row_height - text_height) // 2),
            day,
            font=font,
            fill=(0, 0, 0)
        )

        # Рисуем дату
        date_text = current_date.strftime("%d.%m")
        draw.text(
            (1, table_start_y + i * row_height + 45),  # Левый верхний угол ячейки
            date_text,
            font=font_date,
            fill=(0, 0, 0)
        )

        # Переходим к следующей дате
        current_date += timedelta(days=1)

    
    
    # Время с 6:00 до 23:00
    times = [f"{hour}:00" for hour in range(6, 24)]  
    for i, time in enumerate(times, start=1):
        bbox = draw.textbbox((0, 0), time, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw.text(
            ((i * column_width) + (column_width - text_width) // 2, table_start_y + (row_height - text_height) // 2),
            time,
            font=font,
            fill=(0, 0, 0)
        )

    for event_id, event_data in events.items():
        try:
            event_start = event_data["start"]
            event_end = event_data["end"]
            start_x = (event_start.hour - 6) * column_width
            start_y = (event_start.weekday() + 1) * row_height + table_start_y
            end_x = (event_end.hour - 6) * column_width
            end_y = start_y + row_height

            draw.rectangle([start_x, start_y, end_x, end_y], fill=(123, 231, 128))

            camera_emoji_image = Image.open('src/bot/handlers/camera_emoji.png')

            center_x = (start_x + end_x) // 2
            center_y = (start_y + end_y) // 2

            camera_emoji_resized = camera_emoji_image.resize((20, 16))

            camera_emoji_position = (center_x - 20 // 2, center_y - 16 // 2)
            image.paste(camera_emoji_resized, camera_emoji_position, camera_emoji_resized)

        except Exception as e:
            print(f"Ошибка обработки события {event_id}: {e}")

    image_io = BytesIO()
    image.save(image_io, format="PNG")
    image_io.seek(0)
    return image_io

