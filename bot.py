# Main
import asyncio
import logging

# Env
from dotenv import load_dotenv

# Init and backend
import os
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Handlers
from handlers.base import register_handler_base
from handlers.vps import register_handler_vps
from handlers.balance import register_handler_balance

logger = logging.getLogger(__name__)


async def main():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    logger.info('Getting environment variables')
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    logger.info('Starting Monitoring bot')
    bot = Bot(token=os.getenv('API_BOT_TOKEN'))
    dp = Dispatcher(bot, storage=MemoryStorage())

    logger.info('Register handlers')
    register_handler_base(dp)
    register_handler_balance(dp)
    register_handler_vps(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
