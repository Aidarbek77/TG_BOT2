from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers.start_handler import register_handlers_start
from handlers.homework_handler import register_handlers_homework
from database.db import init_db

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

register_handlers_start(dp)
register_handlers_homework(dp)

init_db()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
