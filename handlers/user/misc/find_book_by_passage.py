from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from data import messages
from keyboards.default import menu_kb
from loader import dp
from states import Menu


@dp.message_handler(Text(equals=[menu_kb.data.find_book_by_passage]), state=Menu.waiting_menu_item_selection)
async def find_book_by_passage(message: Message):
    await message.answer(text=messages.in_development, reply_markup=ReplyKeyboardRemove())
    await Menu.next()
