from aiogram import Bot, Dispatcher, executor
from bot_handlers import register_handlers
import os
from config import load_config

load_config()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
