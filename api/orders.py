import requests
import os


def get_orders():
    """
    Return JSON list with info about ALL orders
    :return:
    """
    return requests.get('https://fornex.com/api/orders/list', {
        'apikey': os.getenv('API_FORNEX_TOKEN')
    }).json()


def get_order_id(name):
    """
    Return current order's id
    :param name:
    :return:
    """
    orders = get_orders()
    for order in orders:
        if order['name'] == name or order['tariff'] == name:
            return order['id']


def get_order_names_or_traffics():
    """
    Return list of names or traffics of all orders for handlers
    :return:
    """
    orders = get_orders()
    return [order['name'] if order['name'] else order['tariff'] for order in orders if order['type'] == 'vps']


def get_order_info(name):
    """
    Representation info about current order
    :param name:
    :return:
    """
    name_order = ''
    status_order = ''
    cost_month_order = ''
    expiration_date_order = ''
    orders = get_orders()
    for order in orders:
        if order['name'] == name['name'] or order['tariff'] == name['name']:
            name_order = order['name'] if order['name'] else order['tariff']
            status_order = order['status']
            cost_month_order = order['cost_month']
            expiration_date_order = order['expiration_date'].split('T')[0]
    return f'Название - {name_order}\nСтатус - {status_order}\n' \
           f'Стоимость в месяц - {cost_month_order}\nАктивен до - {expiration_date_order}'
