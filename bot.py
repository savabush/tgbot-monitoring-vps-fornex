# Main
import asyncio
import logging

# Env
from dotenv import load_dotenv

# Init and backend
import os
from aiogram import Dispatcher, Bot

# Handlers
from handlers.base import register_handler_common
from handlers.guide import register_handler_guide

logger = logging.getLogger(__name__)


async def main():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    logger.error('Getting environment variables')
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    logger.error('Starting R3 bot')
    bot = Bot(token=os.getenv('API_BOT_TOKEN'))
    dp = Dispatcher(bot)

    logger.error('Register handlers')
    register_handler(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
