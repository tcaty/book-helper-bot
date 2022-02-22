from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_inline_url_kb(text: str, url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, url=url)]
        ]
    )
