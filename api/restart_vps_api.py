import requests
import os


def restart_vps_api(order_id):
    """
    Post request to Hard-reset VPS and return status code
    :param order_id:
    :return:
    """
    return requests.post(f'https://fornex.com/api/vps/hard_reset/{order_id}/', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).status_code
