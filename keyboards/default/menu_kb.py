from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dataclasses import dataclass


@dataclass(frozen=True)
class MenuKeyboardData:
    search_book_in_stores: str = 'Искать книгу в магазинах 💵'
    find_book_by_passage: str = 'Найти книгу по отрывку 🔍'


@dataclass(frozen=True)
class MenuKeyboard:
    data: MenuKeyboardData = MenuKeyboardData()
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(MenuKeyboardData.search_book_in_stores)],
            [KeyboardButton(MenuKeyboardData.find_book_by_passage)]
        ],
        resize_keyboard=True
    )


menu_kb = MenuKeyboard()
