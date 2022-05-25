# Aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Api
from api.orders import get_orders, get_order_id, get_order_names_or_traffics
from api.restart_vps_api import restart_vps_api


class NameVPS(StatesGroup):
    wait_for_name = State()


async def vps(msg: types.Message):
    orders = get_orders()
    if len(orders) == 0:
        await msg.answer('У вас нет заказов')
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        buttons = [order['name'] if order['name'] else order['tariff'] for order in orders if order['type'] == 'vps'] + ['Меню']
        keyboard.add(*buttons)
        await msg.answer('Выберите ваш заказ:', reply_markup=keyboard)
        await NameVPS.wait_for_name.set()


async def order_get(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Рестарт', 'Включить', 'Выключить', 'Статус', 'Меню']
    keyboard.add(*buttons)
    await msg.answer('Выберите опцию:', reply_markup=keyboard)


async def restart_vps(msg: types.Message, state: FSMContext):
    name = await state.get_data()
    order_id = get_order_id(name['name'])
    result = restart_vps_api(order_id)
    if result == 200:
        await msg.answer('Перезагрузка сервера')
    else:
        await msg.answer('Ошибка, проверьте ваш заказ')


def register_handler_vps(dp: Dispatcher):
    dp.register_message_handler(vps, lambda msg: msg.text == 'VPS')
    dp.register_message_handler(order_get, lambda msg: msg.text in get_order_names_or_traffics(), state='*')
    dp.register_message_handler(restart_vps, lambda msg: msg.text == 'Рестарт', state='*')