import logging
from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from src.settings import settings
from src.bot.__main__ import bot, dp, start_bot, stop_bot


@asynccontextmanager
async def lifespan(app: FastAPI):
    # logging.info("Starting bot setup...")
    await start_bot()
    webhook_url = settings.get_webhook_url()
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    # logging.info(f"Webhook set to {webhook_url}")
    yield
    # logging.info("Shutting down bot...")
    await bot.delete_webhook()
    await stop_bot()
    # logging.info("Webhook deleted")


app = FastAPI(
    title="Backend Telegram Bot VKS",
    description="",
    lifespan=lifespan,
    debug=settings.debug,
)


@app.post(settings.telegram_bot.WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)