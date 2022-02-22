from aiogram.dispatcher.filters.state import StatesGroup, State


class Menu(StatesGroup):
    waiting_menu_item_selection = State()
