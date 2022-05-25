from aiogram import types, Dispatcher
from api.balance import get_balance


async def balance(msg: types.Message):
    balance_json = get_balance()
    if isinstance(balance_json, dict):
        balance_repr = [f'{balance_json["balance"]} {balance_json["currency"]}']
    else:
        balance_repr = [f'{element["balance"]} {element["currency"]}' for element in balance_json]
    await msg.answer('\n'.join(balance_repr))


def register_handler_balance(dp: Dispatcher):
    dp.register_message_handler(balance, lambda msg: msg.text == 'Баланс')