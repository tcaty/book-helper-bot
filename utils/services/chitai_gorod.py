from typing import List, Tuple

from utils.misc import create_headers
from utils.models import Book

import requests


BASE_URL = 'https://www.chitai-gorod.ru'
HEADERS = create_headers(
        authority='search-v2.chitai-gorod.ru',
        content_type='application/x-www-form-urlencoded'
    )


def transform_data_for_request(data: List[int]) -> List[Tuple[str, str]]:
    result = [
        ('token', '123'),
        ('action', 'read')
    ]
    result.extend([('data[]', str(item)) for item in data or []])
    return result


def get_search_ids(search_query: str) -> List[int]:
    data = {
        'index': 'goods',
        'query': search_query,
        'type': 'common',
        'from': '0',
        'per_page': '24',
        'filters[available]': 'false',
    }

    response = requests.post('https://search-v2.chitai-gorod.ru/api/v3/search/', headers=HEADERS, data=data)
    return response.json().get('ids')


def create_book(book_dict: dict) -> Book:
    sale_price = book_dict.get('sale_price')
    price = book_dict['price']
    author = book_dict.get('author')
    name = book_dict['name']

    return Book(
        store='Читай город',
        url=f"{BASE_URL}{book_dict['link']}",
        title=f'{name} | {author}' if author else name,
        price=sale_price if sale_price else price,
        old_price=price if sale_price else None
    )


def get_books(search_query: str, count: int) -> List[Book]:
    data = transform_data_for_request(get_search_ids(search_query))
    response = requests.post('https://webapi.chitai-gorod.ru/web/goods/extension/list/', headers=HEADERS, data=data)

    if response.status_code == 200:
        result = response.json().get('result')
        if result:
            book_dicts = [result[key] for key in result.keys()]
            books = [create_book(item) for item in book_dicts if item['quantity'] != 0]
            return books[:count]

    return []

