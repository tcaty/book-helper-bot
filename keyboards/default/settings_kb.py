from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dataclasses import dataclass


@dataclass(frozen=True)
class SettingsKeyboardData:
    send_settings: str = 'Показать мои настройки 👁'
    change_settings: str = 'Изменить настройки ⚙️'


@dataclass(frozen=True)
class SettingsKeyboard:
    data: SettingsKeyboardData = SettingsKeyboardData()
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(SettingsKeyboardData.send_settings)],
            [KeyboardButton(SettingsKeyboardData.change_settings)]
        ],
        resize_keyboard=True
    )


settings_kb = SettingsKeyboard()
