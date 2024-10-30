from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart

async def start(message: types.Message):
    await message.answer("Привет! Для отправки домашнего задания введите ваше имя.")
    await HomeworkStates.waiting_for_name.set()

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
