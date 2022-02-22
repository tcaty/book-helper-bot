from aiogram import Dispatcher

from data.config import ADMIN_CHAT_ID


async def startup_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id=ADMIN_CHAT_ID, text='Бот запущен')
