from aiogram.types import Update, ReplyKeyboardRemove

from data import messages
from loader import dp
from utils.misc import write_error


@dp.errors_handler()
async def errors_handler(update: Update, exception):
    """
    Здесь реализован простенький метод обработки исключение.
    То есть при возникновении исключения:
        1) Убирается клавиатура
        2) Сбрасывается текущее состояние
        3) Информация об исключении записывается в файл

    :param update: обновление от пользователя
    :param exception: исключение
    :return:
    """

    message = update.get_current().message

    await message.answer(text=messages.error, reply_markup=ReplyKeyboardRemove())
    await dp.storage.reset_state(chat=message.chat.id)

    write_error(
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        chat_id=message.chat.id,
        message_text=message.text,
        exception=exception
    )
