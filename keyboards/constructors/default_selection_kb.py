from dataclasses import dataclass, field
from typing import List, Union, Any
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.misc import two_level_map


@dataclass(frozen=True)
class DefaultSelectionKeyboardItem:
    """
    Данный класс является вспомогательным для класса DefaultValueKeyboard.
    Он нужен для того, чтобы за кнопками были закреплены любые типы и структуры данных.
    """
    text: str = field(init=True)
    value: Any = field(init=True)


class DefaultSelectionKeyboard:
    """
    Данный класс-конструктор предназначен для создания клавиатур, состоящих из кнопок,
    нажатие на которые переводит пользователя в одно и то же дальнейшее состояние.

    После нажатия на кнопку, пользователем отправляется сообщение,
    мы заведомо уверены, что в следующий обработчик попадёт только сообщение с текстом кнопки,
    так как используем состояния. Благодаря методу get_value() можно получить значение,
    которое закреплено за полученным текстом.
    """

    __items: List[Union[DefaultSelectionKeyboardItem]]
    __keyboard: ReplyKeyboardMarkup

    def __init__(self, items: List[List[Union[DefaultSelectionKeyboardItem]]]):
        self.__items = [item for row in items for item in row]
        self.__keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=two_level_map(items, lambda item: KeyboardButton(item.text), True)
        )

    def get_texts(self) -> List[str]:
        return [item.text for item in self.__items]

    def get_value(self, text: str) -> Any:
        for item in self.__items:
            if item.text == text:
                return item.value

    @property
    def items(self) -> List[Union[DefaultSelectionKeyboardItem]]:
        return self.__items

    @property
    def keyboard(self):
        return self.__keyboard
