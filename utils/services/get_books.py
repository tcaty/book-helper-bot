from typing import List

from utils.models import Book
from utils.services import chitai_gorod, ozon, wildberries


def sort_books(books: List[Book], reverse: bool) -> List[Book]:
    return sorted(books, key=lambda book: book.price, reverse=reverse)


def get_books(search_query: str, count: int, reverse: bool) -> List[Book]:
    books = []

    books.extend(chitai_gorod.get_books(search_query, count))
    books.extend(ozon.get_books(search_query, count))
    books.extend(wildberries.get_books(search_query, count))

    return sort_books(books, reverse)
