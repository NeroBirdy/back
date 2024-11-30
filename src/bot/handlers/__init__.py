from aiogram import Dispatcher
from .start import router as start_routers
from .vks import router as vks_routers


def register_routes(dp: Dispatcher):
    dp.include_router(start_routers)
    dp.include_router(vks_routers)