from aiogram import types, F, Router
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

