import requests
import os


def get_orders():
    return requests.get('https://fornex.com/api/orders/list', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).json()


def get_order_id(name):
    orders = get_orders()
    for order in orders:
        if order['name'] == name or order['tariff'] == name:
            return order['id']
    return 'Проверьте Ваши заказы'


def get_order_names_or_traffics():
    orders = get_orders()
    return [order['name'] if order['name'] else order['tariff'] for order in orders if order['type'] == 'vps']
