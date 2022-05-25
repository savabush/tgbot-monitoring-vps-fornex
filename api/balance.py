import requests
import os


def get_balance():
    return requests.get('https://fornex.com/api/account/balance', {
       'apikey': os.getenv('API_FORNEX_TOKEN')
    }).json()
