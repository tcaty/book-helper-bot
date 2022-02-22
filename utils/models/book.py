from dataclasses import dataclass, field


@dataclass(frozen=True)
class Book:
    """
    Данный класс является моделью книги, массив этих объектов
    является результатом работы каждого взаимодействия с api магазина.
    """

    store: str = field(init=True)
    url: str = field(init=True)
    title: str = field(init=True)
    price: int = field(init=True)
    old_price: int = field(init=True)

    def get_description(self) -> str:
        old_price = f'Старая цена: <s>{str(self.old_price)} ₽</s> \n' if self.old_price else ''
        description = f'{self.title} \n\n' \
                      f'{old_price}' \
                      f'Цена: <b>{str(self.price)} ₽</b>'
        return description

    def __str__(self) -> str:
        string = ''
        for value in self.__dict__.values():
            string = string + str(value) + '\n'
        return string
