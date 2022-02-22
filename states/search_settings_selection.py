from aiogram.dispatcher.filters.state import State, StatesGroup


class SearchSettingsSelection(StatesGroup):
    waiting_count = State()
    waiting_sorting_reverse = State()
