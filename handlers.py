from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer('Привет! Этот вычисляет данные для фрейзерного станка.\nНо прежде чем ты начнешь его использовать, тебе необходимо ввести пароль.')



