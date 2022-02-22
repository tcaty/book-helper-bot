from typing import List, Tuple, Union
from utils.misc import create_headers
from utils.models import Book

import requests


BASE_URL = 'https://www.wildberries.ru'
HEADERS = create_headers(
    authority='wbxsearch.wildberries.ru',
    content_type='application/json'
)


def get_request_settings(search_query: str) -> Union[dict[str, Union[str, None]], None]:
    params = (('query', search_query),)
    response = requests.get('https://wbxsearch.wildberries.ru/exactmatch/v2/common', headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        query = data.get('query')
        shard_key = data.get('shardKey')
        return {'query': query, 'shard_key': shard_key}

    return {'query': None, 'shard_key': None}


def transform_query(query: str) -> List:
    pairs = query.split('&')
    return [tuple(pair.split('=')) for pair in pairs]


def create_params(query: str, shard_key: str) -> Tuple:
    params = [
        ('spp', '0'),
        ('regions', '64,86,83,4,38,30,33,70,22,31,66,68,1,82,48,40,69,80'),
        ('stores','117673,122258,122259,125238,125239,125240,117401,124731,507,3158,117501,120762,120602,121709,130744,159402,2737,117986,1733,686,132043'),
        ('pricemarginCoeff', '1.0'),
        ('reg', '0'),
        ('appType', '1'),
        ('offlineBonus', '0'),
        ('onlineBonus', '0'),
        ('emp', '0'),
        ('locale', 'ru'),
        ('lang', 'ru'),
        ('curr', 'rub'),
        ('couponsGeo', '2,12,3,18,22,21'),
        ('dest', '-1029256,-81993,-4775559,-5663284'),
        ('page', '1'),
        ('sort', 'rate'),
        ('xsubject', '381'),
    ]

    if shard_key == 'merger':
        params.extend(transform_query(query))
    else:
        params.append(('preset', query.split('=')[1]))

    return tuple(params)


def create_book(book_dict: dict) -> Book:
    sale_price = book_dict['salePriceU'] // 100
    price = book_dict['priceU'] // 100

    return Book(
        store='Wildberries',
        url=f'{BASE_URL}/catalog/{book_dict["id"]}/detail.aspx?targetUrl=XS',
        title=book_dict['name'],
        price=sale_price,
        old_price=price if sale_price != price else None
    )


def get_books(search_query: str, count: int) -> List[Book]:
    request_settings = get_request_settings(search_query)
    query = request_settings['query']
    shard_key = request_settings['shard_key']

    if query:
        params = create_params(query, shard_key)
        response = requests.get(
            f'https://wbxcatalog-ru.wildberries.ru/{shard_key}/catalog',
            headers=HEADERS,
            params=params
        )

        if response.status_code == 200:
            book_dicts = response.json().get('data').get('products')
            books = [create_book(book_dict) for book_dict in book_dicts]
            return books[:count]

    return []


if __name__ == '__main__':
    for item in get_books('похититель теней', 5):
        print(item)

