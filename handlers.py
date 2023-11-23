import dp
from aiogram import types, F, Router
from aiogram.client import bot
from aiogram.types import Message
from aiogram.filters import Command
import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer_sticker(sticker=text.start_sticker)
    await msg.answer(text.initial_message,
                     parse_mode="HTML",
                     reply_markup=kb.keyboard_authentication)
    await msg.delete()

@router.message(Command("help"))
async def help_command(msg: Message):
    await msg.reply(text.HELP_COMMANDS)
    await msg.delete()

@router.message(Command("role"))
async def get_user_role(msg: Message):
    await msg.reply(text.role, reply_markup=kb.keyboard_role)

@router.callback_query
async def callback_handler(query: types.CallbackQuery):
    role = query.data

    if role == "boss_role":
        await bot.send_message(query.from_user.id, "Buttons for Boss")
    elif role == "designer_role":
        await bot.send_message(query.from_user.id, "Buttons for Designer")
    elif role == "accountant_role":
        await bot.send_message(query.from_user.id, "Buttons for Accountant")
    elif role == "developer_role":
        await bot.send_message(query.from_user.id, "Buttons for Developer")
