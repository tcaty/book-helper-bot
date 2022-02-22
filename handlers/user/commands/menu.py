from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from data import messages
from data.commands import commands
from keyboards.default import menu_kb
from loader import dp
from states import Menu


@dp.message_handler(Command(commands.menu.name))
async def menu(message: Message):
    await message.answer(text=messages.menu, reply_markup=menu_kb.keyboard)
    await Menu.waiting_menu_item_selection.set()
