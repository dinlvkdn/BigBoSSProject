from idlelib import query

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

@router.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    user_id =callback.from_user.id
    if callback.data == "boss_role":
        await callback.answer(text="Ви обрали роль - боса")
        # await msg.reply(text.boss, reply_markup=kb.keyboard_boss)
    elif callback.data == "designer_role":
        await callback.answer(text="Ви обрали роль - дизайнера")
        # await bot.send_message(user_id, "Оберіть опцію для дизайнера:", reply_markup=kb.keyboard_designer)
        # await bot.send_message(user_id, text.designer, reply_markup=kb.keyboard_designer)
        # await msg.reply(text.designer, reply_markup=kb.keyboard_designer)
    elif callback.data == "accountant_role":
        await callback.answer(text="Ви обрали роль - бухгалтера")
        await bot.send_message(user_id, text.designer, reply_markup=kb.keyboard_designer)
        # await msg.reply(text.accountant, reply_markup=kb.keyboard_accountant)
    elif callback.data == "developer_role":
        await callback.answer(text="Ви обрали роль - розробника")
        await bot.send_message(user_id, text.designer, reply_markup=kb.keyboard_designer)
        # await msg.reply(text.developer, reply_markup=kb.keyboard_developer)

