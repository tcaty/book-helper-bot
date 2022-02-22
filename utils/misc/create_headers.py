from typing import Dict

from user_agent import generate_user_agent


def create_headers(authority: str, content_type: str) -> Dict[str, str]:
    return {
        'connection': 'keep-alive',
        'authority': authority,
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'x-o3-app-name': 'dweb_client',
        'sec-ch-ua-mobile': '?0',
        'user-agent': generate_user_agent(),
        'content-type': content_type,
        'accept': '*/*',
        'x-o3-app-version': 'release_17-1\'-\'2022_ac08d7e1',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    }

