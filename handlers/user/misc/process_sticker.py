from aiogram.types import Message

from data import messages
from loader import dp


@dp.message_handler(content_types=['sticker'])
async def process_sticker(message: Message):
    await message.answer_sticker(sticker=messages.cat_ghoul)


