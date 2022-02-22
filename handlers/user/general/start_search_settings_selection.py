from aiogram.types import Message

from data import messages
from keyboards.default import count_selection_kb
from states import SearchSettingsSelection


async def start_search_settings_selection(message: Message):
    await message.answer(messages.select_count, reply_markup=count_selection_kb.keyboard)
    await SearchSettingsSelection.waiting_count.set()
