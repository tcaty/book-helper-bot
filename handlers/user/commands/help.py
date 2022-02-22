from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from data import messages
from data.commands import commands
from loader import dp


@dp.message_handler(Command(commands.help.name))
async def help(message: Message):
    await message.answer(text=messages.help)
