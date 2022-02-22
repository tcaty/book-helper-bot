from aiogram import Dispatcher

from data.config import ADMIN_CHAT_ID


async def shutdown_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id=ADMIN_CHAT_ID, text='Работа бота остановлена')
