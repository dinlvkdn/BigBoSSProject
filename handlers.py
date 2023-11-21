from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

# обробник вхідних повідомлень
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Вітаємо!Для аутентифікації Вам потрібно перейти за посиланням, та слідувати вказівкам. Після цього Ви зможете користуватися нашим ботом")
    # bot.send_message(msg.chat.id, "Text")        можна і так записати

# обробник вхідних повідомлень реагує на всі повідомлення, оскільки  msg: Message
@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"ID: {msg.from_user.id}")


