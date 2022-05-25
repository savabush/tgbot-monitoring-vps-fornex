import requests
import os


def get_status_info(order_id):
    """
    Return JSON status info about order
    :param order_id:
    :return:
    """
    return requests.get(f'https://fornex.com/api/vps/status/{order_id}/', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).json()
