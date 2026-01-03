import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

# Aiogram imports
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Importing routers
from handlers import user_router # , admin_router, payment_router

# Bot token obtained via .env
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main() -> None:
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # dp.include_router(admin_router)
    dp.include_router(user_router)
    # dp.include_router(payment_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())