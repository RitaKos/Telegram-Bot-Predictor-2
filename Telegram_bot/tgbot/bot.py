import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.utils.helper import HelperMode

from Telegram_bot.tgbot.config import load_config
from filters.admin import AdminFilter
from handlers.admin import register_admin
from handlers.user import register_user
from handlers.user import register_about
from handlers.user import register_topics
from handlers.user import register_topic1
from handlers.user import register_user_mess
from middlewares.db import DbMiddleware

logger = logging.getLogger(__name__)

def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())

def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_about(dp)
    register_topics(dp)
    register_topic1(dp)
    register_user_mess(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")


    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot)

    bot['config'] = config
    #bot.set_my_commands(['/start','/topics','/about','/end'])

    register_all_filters(dp)

    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()

    finally:
        await bot.get_session()
        #await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
