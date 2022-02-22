from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram import Bot, Dispatcher, types
from data.config import BOT_TOKEN, DEVELOPMENT


bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage() if DEVELOPMENT else RedisStorage2()
dp = Dispatcher(bot, storage=storage)
