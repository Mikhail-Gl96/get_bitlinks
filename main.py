import requests
import os
import argparse

from urllib.parse import urlparse

from dotenv import load_dotenv


URL_BITLY = 'https://api-ssl.bitly.com/v4'


def get_user_info():
    url_user = f'{URL_BITLY}/user'
    response = requests.get(url_user, headers=headers)
    response.raise_for_status()
    return response.json()


def create_bitlink(url: str):
    url_bitlinks = f"{URL_BITLY}/bitlinks"
    params = {
        "long_url": url,
        "group_guid": get_user_info()["default_group_guid"],
        "domain": "bit.ly",
        "title": "test_link"
    }
    response = requests.post(url=url_bitlinks, headers=headers, json=params)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def create_shorten_link(url: str):
    url_shorten = f"{URL_BITLY}/shorten"
    params = {
        "long_url": url,
        "group_guid": get_user_info()["default_group_guid"],
        "domain": "bit.ly",
        "title": "test_link"
    }
    response = requests.post(url=url_shorten, headers=headers, json=params)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def get_count_clicks(bitlink: str, unit: str = 'day', units=False):
    url_shorten = f"{URL_BITLY}/bitlinks/{bitlink}/clicks/summary"
    params = {
        "unit": unit,
        "units": units if units else -1
    }
    response = requests.get(url=url_shorten, headers=headers, params=params)
    response.raise_for_status()
    total_clicks = response.json()["total_clicks"]
    return total_clicks


def get_shorten_link_or_count_clicks(bitlink: str):
    # Если перезапишем переменную bitlink, то в случае не битлинка
    # потеряем протокол и не сможем сделать битлинк, поэтому сделаем отдельную переменную
    bitlink_no_protocol = urlparse(bitlink).netloc + urlparse(bitlink).path

    is_bitlink = check_is_bitlink(bitlink=bitlink_no_protocol)

    if is_bitlink:
        answer = get_count_clicks(bitlink_no_protocol)
        return f"Total clicks: {answer}"
    else:
        answer = create_bitlink(url=bitlink)
        return f"Bitlink: {answer}"


def check_is_bitlink(bitlink: str):
    url_shorten = f"{URL_BITLY}/bitlinks/{bitlink}"
    response = requests.get(url=url_shorten, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()

    BITLY_AUTH_TOKEN = os.getenv("BITLY_AUTH_TOKEN")
    headers = {
        "Authorization": BITLY_AUTH_TOKEN
    }

    parser = argparse.ArgumentParser(description='Bitly command line program')
    
    # Как требуется по заданию
    parser.add_argument('link', type=str, help='link')

    args = parser.parse_args()

    url = args.link

    try:
        answer = get_shorten_link_or_count_clicks(bitlink=url)
        print(answer)
    except requests.exceptions.HTTPError as e:
        print('Error: ', e)
