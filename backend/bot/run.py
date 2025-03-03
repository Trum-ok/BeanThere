import sys
import logging

import signal
import asyncio
from aiogram import Dispatcher
from models import BeanBot

from logs import logger
from config import Config
from handlers import routers
from middlewares import AdminMiddleware


async def run():
    config = Config()
    dp = Dispatcher()
    bot = BeanBot(token=config.TG_TOKEN, db=...)

    dp.include_routers(*routers)
    dp.message.middleware(AdminMiddleware())

    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            close_bot_session=True
        )
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped by signal")
    except Exception as e:
        logger.critical("Unexpected error", exc_info=e)
    finally:
        await bot.session.close()


def handle_exit(signum, frame):
    raise SystemExit


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    # logger.info("Starting bot...")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run())
