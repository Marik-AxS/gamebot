from database.models import async_main, add_game
import asyncio 
import sys,logging 
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.commands import router

async def main():
    # await async_main()
    #await add_game()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())