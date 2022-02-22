from aiogram.dispatcher.filters.state import StatesGroup, State


class Settings(StatesGroup):
    waiting_settings_menu_selection = State()
