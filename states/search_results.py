from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchResults(StatesGroup):
    waiting_author_and_title = State()
