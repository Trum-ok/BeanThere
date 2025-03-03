from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет')
