from typing import Union


class SearchSettings:
    """
    Данный класс используется для избежания фантомных строк в коде.
    Названия его полей используются в качестве ключей в shelve хранилище, а так же в state.
    Благодаря SearchSettings.get_count_name() мы можем быть уверены в том,
    что и в хранилище и в state используется один и тот же ключ.
    """

    __count: Union[str, int] = 'count'
    __sorting_reverse: Union[str, bool] = 'sorting_reverse'

    def __init__(self, count: int, sorting_reverse: bool):
        self.__count = count
        self.__sorting_reverse = sorting_reverse

    @property
    def count(self) -> Union[int]:
        return self.__count

    @property
    def sorting_reverse(self) -> Union[bool]:
        return self.__sorting_reverse

    @staticmethod
    def count_name() -> str:
        return SearchSettings.__count

    @staticmethod
    def sorting_reverse_name() -> str:
        return SearchSettings.__sorting_reverse

