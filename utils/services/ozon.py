from typing import List

from utils.misc import create_headers, quote_text
from utils.models import Book

import json
import requests


BASE_URL = 'https://www.ozon.ru'
HEADERS = create_headers(
    authority='www.ozon.ru',
    content_type='application/json'
)


def create_url(search_query: str) -> str:
    text = quote_text(search_query)
    return f'/category/knigi-16500/?category_was_predicted=true&from_global=true&text={text}'


def is_book_available(book_dict: dict) -> bool:
    if book_dict:
        return int(book_dict.get('stock') or 0) > 0
    return False


def create_book(book_dict: dict) -> Book:
    price = book_dict['price']
    final_price = book_dict['finalPrice']

    return Book(
        store='Ozon',
        url=f'{BASE_URL}{book_dict["link"]}',
        title=book_dict['title'],
        price=final_price,
        old_price=price if price != final_price else None
    )


def get_books(search_query: str, count: int) -> List[Book]:
    params = (
        ('page_changed', 'true'),
        ('url', create_url(search_query)),
    )
    response = requests.get('https://www.ozon.ru/api/composer-api.bx/page/json/v2', headers=HEADERS, params=params)

    if response.status_code == 200:
        data = list(response.json().get('trackingPayloads').values())
        if data:
            book_dicts = [json.loads(item) for item in data if item]
            books = [create_book(book_dict) for book_dict in book_dicts if is_book_available(book_dict)]
            return books[:count]

    return []
