import asyncio
import logging
from aiogram import Dispatcher, Bot
# from aiogram.client.session.aiohttp import AiohttpSession
# from aiogram.client.telegram import TelegramAPIServer

from config import settings
from common.cmd_list import private

# from app.database.init import create_db, drop_db, session_maker
from handlers.commands import command_router
from handlers.user_private import user_private_router
from handlers.portfolio import portfolio_router
from handlers.service import service_router
# from app.handlers.admin_private import admin_router

# from app.middlewares.db import DataBaseSession
#########################################################
#----------------------run.py---------------------------#


# Initialize Dispatcher

dp = Dispatcher()



# Include Routers
dp.include_router(command_router)
# dp.include_router(admin_router)
dp.include_router(service_router)
dp.include_router(portfolio_router)
dp.include_router(user_private_router)



# main function
async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    # session = AiohttpSession(
    #     api=TelegramAPIServer.from_base('https://tgrasp.co')
    # )
    
    bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
    
    await bot.set_my_commands(private)
    # dp.update.middleware(DataBaseSession(session_pool=session_maker))
    # Start the bot
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
    

# startup and shutdown handlers
async def on_startup(bot):
    logging.info("Starting bot")
    
    # is_dropped = False
    # if is_dropped:
    #     await drop_db()
        
    # await create_db()


async def on_shutdown(bot):
    logging.info("Shutting down bot")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("error")