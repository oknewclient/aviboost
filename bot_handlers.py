from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.lower() == "привет")
async def greet_user(message: Message):
    await message.answer("Привет! Я бот, готов к работе.")
