from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

calendar_router = Router(name="calendar")


@calendar_router.message(Command("event"))
async def handle_event(message: Message):
    pass
