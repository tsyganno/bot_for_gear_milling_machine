import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from os import getenv, path
from dotenv import load_dotenv

from handlers import router

load_dotenv()

""" Логи """
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
work_dir = path.dirname(path.abspath(__file__))
out = open('prod.log', 'w+')


API_TOKEN = getenv('BOT_TOKEN')


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    logger.info('start_polling')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())