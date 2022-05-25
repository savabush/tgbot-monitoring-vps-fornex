from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as fmt


async def cmd_start(msg: types.Message, state: FSMContext):
    await state.finish()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ['VPS', 'Баланс', 'О боте']
    keyboard.add(*buttons)
    await msg.answer('Меню:', reply_markup=keyboard)
    await msg.delete()


async def about(msg: types.Message):
    await msg.answer(f'{fmt.hide_link("github.com/savabush/")}'
                     f'Бот для получения статистики и управления VPS конфигурациями через API Fornex.'
                     f'\n\nMade by savabush', parse_mode=types.ParseMode.HTML)


def register_handler_base(dp: Dispatcher):
    dp.register_message_handler(cmd_start, lambda msg: msg.text == 'Меню' or msg.text == '/start', state='*')
    dp.register_message_handler(about, lambda msg: msg.text == 'О боте')
