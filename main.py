from aiogram import Dispatcher, executor
from utils.bot_life_cycle.startup import startup_notify, set_default_commands
from utils.bot_life_cycle.shutdown import shutdown_notify, close_storage_connection
from loader import dp

import states
import handlers


async def on_startup(dp: Dispatcher):
    await set_default_commands(dp)
    await startup_notify(dp)


async def on_shutdown(dp: Dispatcher):
    await close_storage_connection(dp)
    await shutdown_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
