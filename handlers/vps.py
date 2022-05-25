# Aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Api
from api.orders import get_orders, get_order_id, get_order_names_or_traffics, get_order_info
from api.restart_vps_api import restart_vps_api
from api.status_vps_api import get_status_info
from api.on_off_vps_api import turn_on_vps_api, turn_off_vps_api


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

    name = await state.get_data()
    current_order_info = get_order_info(name)

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Рестарт', 'Включить', 'Выключить', 'Статус', 'Меню']
    keyboard.add(*buttons)
    await msg.answer(current_order_info)
    await msg.answer('Выберите опцию:', reply_markup=keyboard)


async def restart_vps(msg: types.Message, state: FSMContext):
    name = await state.get_data()
    order_id = get_order_id(name['name'])
    result = restart_vps_api(order_id)
    if result == 200:
        await msg.answer('Перезагрузка сервера')
    else:
        await msg.answer('Ошибка, проверьте ваш заказ')


async def status_vps(msg: types.Message, state:FSMContext):
    name = await state.get_data()
    order_id = get_order_id(name['name'])
    result = get_status_info(order_id)
    if result['status'] == 'on':
        await msg.answer('VPS работает')
    else:
        await msg.answer('VPS выключен')


async def turn_on_vps(msg: types.Message, state: FSMContext):
    name = await state.get_data()
    order_id = get_order_id(name['name'])
    result = turn_on_vps_api(order_id)
    if result == 200:
        await msg.answer('VPS включен')
    else:
        await msg.answer('Ошибка, проверьте ваш заказ')


async def turn_off_vps(msg: types.Message, state: FSMContext):
    name = await state.get_data()
    order_id = get_order_id(name['name'])
    result = turn_off_vps_api(order_id)
    if result == 200:
        await msg.answer('VPS выключен')
    else:
        await msg.answer('Ошибка, проверьте ваш заказ')


def register_handler_vps(dp: Dispatcher):
    dp.register_message_handler(vps, lambda msg: msg.text == 'VPS')
    dp.register_message_handler(order_get, lambda msg: msg.text in get_order_names_or_traffics(), state='*')
    dp.register_message_handler(restart_vps, lambda msg: msg.text == 'Рестарт', state='*')
    dp.register_message_handler(status_vps, lambda msg: msg.text == 'Статус', state='*')
    dp.register_message_handler(turn_on_vps, lambda msg: msg.text == 'Включить', state='*')
    dp.register_message_handler(turn_off_vps, lambda msg: msg.text == 'Выключить', state='*')
