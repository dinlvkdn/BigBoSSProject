
import asyncio
# для логінації
import logging

import executor
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router


# Функція для запуску бота
async def main():
    # створюємо об'єкт бота з токеном
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # створюємо об'єкт диспетчера   MemoryStorage()- дані які не зберігаються в бд будуть стерті при запуску
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    # видаляємо всі оновлення які пройщлт після останнього завершення роботи(для обробки тільки тих повідомлень які прийшли під час роботи а не за весь час)
    await bot.delete_webhook(drop_pending_updates=True)
    # запуск бота
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())












# бот продовжує слухати нас
# bot.polling()