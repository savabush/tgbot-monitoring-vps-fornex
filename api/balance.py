import requests
import os


def get_balance():
    """
    GET request for getting json data about balance info
    :return:
    """
    return requests.get('https://fornex.com/api/account/balance', {
       'apikey': os.getenv('API_FORNEX_TOKEN')
    }).json()
