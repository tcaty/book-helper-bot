from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from data import messages
from keyboards.default import count_selection_kb, sorting_reverse_selection_kb
from loader import dp
from states import SearchSettingsSelection
from utils.models import SearchSettings
from utils.shelve_storage import shelve_storage


@dp.message_handler(Text(equals=count_selection_kb.get_texts()), state=SearchSettingsSelection.waiting_count)
async def set_count(message: Message, state: FSMContext):
    await state.update_data({SearchSettings.count_name(): count_selection_kb.get_value(message.text)})
    await message.answer(messages.select_sorting_reverse, reply_markup=sorting_reverse_selection_kb.keyboard)
    await SearchSettingsSelection.waiting_sorting_reverse.set()


@dp.message_handler(Text(equals=sorting_reverse_selection_kb.get_texts()), state=SearchSettingsSelection.waiting_sorting_reverse)
async def set_sorting_reverse(message: Message, state: FSMContext):
    await state.update_data({SearchSettings.sorting_reverse_name(): sorting_reverse_selection_kb.get_value(message.text)})

    async with state.proxy() as data:
        search_settings = SearchSettings(
            count=data[SearchSettings.count_name()],
            sorting_reverse=data[SearchSettings.sorting_reverse_name()]
        )
        shelve_storage.add_search_settings(message.chat.id, search_settings)

    await message.answer(text=messages.search_settings_saved, reply_markup=ReplyKeyboardRemove())

    await SearchSettingsSelection.next()
    await state.reset_state()
