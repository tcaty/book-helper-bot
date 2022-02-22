from data.config import SHELVE_STORAGE_PATH
from utils.models import SearchSettings

import shelve


class ShelveStorage:
    """
    Данный класс является удобным интерфейсом для работы с shelve хранилищем
    С внешним миром он обменивается типом данных SearchSettings
    """

    def __init__(self, storage_path: str):
        self.__storage_path = storage_path

    def is_in_storage(self, chat_id: int) -> bool:
        with shelve.open(self.__storage_path) as storage:
            return bool(storage.get(str(chat_id), None))

    def add_search_settings(self, chat_id: int, search_settings: SearchSettings) -> None:
        with shelve.open(self.__storage_path) as storage:
            storage[str(chat_id)] = {
                SearchSettings.count_name(): search_settings.count,
                SearchSettings.sorting_reverse_name(): search_settings.sorting_reverse
            }

    def get_search_settings(self, chat_id: int) -> SearchSettings:
        with shelve.open(self.__storage_path) as storage:
            item = storage.get(str(chat_id))
            return SearchSettings(
                count=item[SearchSettings.count_name()],
                sorting_reverse=item[SearchSettings.sorting_reverse_name()]
            )


shelve_storage = ShelveStorage(SHELVE_STORAGE_PATH)
