from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.settings import settings
from src.bot.handlers import register_routes

storage = MemoryStorage()

bot = Bot(token=settings.telegram_bot.BOT_TOKEN)
dp = Dispatcher(storage=storage)

register_routes(dp)

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