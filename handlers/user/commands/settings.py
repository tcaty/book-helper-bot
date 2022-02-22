from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from data import messages
from data.commands import commands
from handlers.user.general import start_search_settings_selection
from keyboards.default import settings_kb
from loader import dp
from states import Settings
from utils.shelve_storage import shelve_storage


@dp.message_handler(Command(commands.settings.name))
async def settings(message: Message):
    await message.answer(text=messages.menu, reply_markup=settings_kb.keyboard)
    await Settings.waiting_settings_menu_selection.set()


@dp.message_handler(Text(equals=settings_kb.data.send_settings), state=Settings.waiting_settings_menu_selection)
async def send_settings(message: Message):
    search_settings = shelve_storage.get_search_settings(message.chat.id)
    sorting = messages.desc if search_settings.sorting_reverse else messages.asc

    await message.answer(
        text=messages.your_search_settings % (search_settings.count, sorting),
        reply_markup=ReplyKeyboardRemove()
    )
    await Settings.next()


@dp.message_handler(Text(equals=settings_kb.data.change_settings), state=Settings.waiting_settings_menu_selection)
async def change_settings(message: Message):
    await start_search_settings_selection(message)

