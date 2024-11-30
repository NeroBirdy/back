from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsPrivateFilter(BaseFilter):
    async def __call__(self, obj: Message):
        return obj.chat.type == 'private'

class WebAppDataFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return bool(message.web_app_data)
