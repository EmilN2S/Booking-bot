from os import getenv
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing from the .env file")

dp = Dispatcher()

async def main():
    async with Bot(token=TOKEN) as bot:
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())