from aiogram import Router, flags
from aiogram.types import Message
from aiogram.filters import Command

health_router = Router(name='health')


@health_router.message(Command("health"))
@flags.admin(is_admin=True)
async def health_check(message: Message):
    await message.answer("OK")
