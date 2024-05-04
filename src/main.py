from bot import bot

from bot.bot import bot
import asyncio
from bot.handlers import dp


ALLOWED_UPDATES = ['message']

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    
if __name__ == '__main__':
    asyncio.run(main())