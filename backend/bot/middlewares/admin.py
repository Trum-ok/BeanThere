from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message, TelegramObject

from config import Config

ADMINS = Config.ADMINS


class AdminMiddleware(BaseMiddleware):
    """
    Check if user is admin
    """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        admin_flag = get_flag(data, "admin")
        if admin_flag is not None:
            if admin_flag["is_admin"]:
                if event.chat.id in ADMINS:
                    return await handler(event, data)
                else:
                    return None
        else:
            return await handler(event, data)
