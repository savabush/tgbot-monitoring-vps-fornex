import requests
import os


def restart_vps_api(order_id):
    return requests.post(f'https://fornex.com/api/vps/hard_reset/{order_id}/', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).status_code
