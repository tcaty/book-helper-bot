from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from data import messages
from handlers.user.general import start_search_settings_selection
from keyboards.default.menu_kb import MenuKeyboardData
from loader import dp
from states import Menu, SearchResults
from utils.shelve_storage import shelve_storage


@dp.message_handler(Text(equals=[MenuKeyboardData.search_book_in_stores]), state=Menu.waiting_menu_item_selection)
async def search_book_in_stores(message: Message):
    if shelve_storage.is_in_storage(str(message.chat.id)):
        await message.answer(text=messages.enter_author_and_title, reply_markup=ReplyKeyboardRemove())
        await SearchResults.waiting_author_and_title.set()
    else:
        await start_search_settings_selection(message)
