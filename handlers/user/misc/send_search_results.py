from aiogram.types import Message

from data import messages
from keyboards.constructors import create_inline_url_kb
from loader import dp
from states import SearchResults
from utils.models import Book
from utils.services import get_books
from utils.shelve_storage import shelve_storage


async def send_book(book: Book, message: Message):
    await message.answer(
        text=book.get_description(),
        reply_markup=create_inline_url_kb(book.store, book.url)
    )


@dp.message_handler(state=SearchResults.waiting_author_and_title)
async def send_search_results(message: Message):
    search_settings = shelve_storage.get_search_settings(message.chat.id)
    books = get_books(message.text, search_settings.count, search_settings.sorting_reverse)
    books_len = len(books)

    if books_len > 0:
        for i in range(books_len):
            await send_book(books[i], message)
            if i != books_len - 1:
                await message.answer(messages.separator)
    else:
        await message.answer(messages.book_not_found)

    await SearchResults.next()

