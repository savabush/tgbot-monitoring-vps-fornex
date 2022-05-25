import requests
import os


def turn_on_vps_api(order_id):
    """
    POST request to turn ON VPS
    :param order_id:
    :return:
    """
    return requests.post(f'https://fornex.com/api/vps/start/{order_id}/', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).status_code


def turn_off_vps_api(order_id):
    """
    POST request to turn OFF VPS
    :param order_id:
    :return:
    """
    return requests.post(f'https://fornex.com/api/vps/stop/{order_id}/', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).status_code
