from aiogram import Dispatcher


async def close_storage_connection(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
