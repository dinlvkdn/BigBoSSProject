from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import kb
import text
from sqlite import db_start, create_profile, edit_profile, get_role_and_id

async def on_startup(dp):
    await db_start()


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer_sticker(sticker=text.start_sticker)
    await msg.answer(text.initial_message,
                     parse_mode="HTML",
                     reply_markup=kb.keyboard_role)
    await msg.delete()
    # записати в базу даних id користувача
    await create_profile(user_id=msg.from_user.id)

@router.message(Command("help"))
async def help_command(msg: Message):
    await msg.reply(text.HELP_COMMANDS)
    await msg.delete()

# @router.message(Command("role"))
# async def get_user_role(msg: Message):
#     await msg.reply(text.role, reply_markup=kb.keyboard_role)



@router.callback_query(lambda c: c.data in {"boss_role", "accountant_role", "designer_role", "developer_role"})
async def role_selected_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    selected_role = callback_query.data
    await create_profile(user_id, role=selected_role)


    if selected_role == "boss_role":
        await callback_query.answer(text=text.role_bos)
        await callback_query.message.answer("Бос, оберіть опцію:", reply_markup=kb.keyboard_boss)

    elif selected_role == "accountant_role":
        await callback_query.answer(text="Ви обрали роль - Бухгалтер")

    elif selected_role == "designer_role":
        await callback_query.answer(text="Ви обрали роль - Дизайнер")
        await callback_query.message.answer("Дизайнер, оберіть опцію:", reply_markup=kb.keyboard_designer)

    elif selected_role == "developer_role":
        await callback_query.answer(text="Ви обрали роль - розробника")

    await callback_query.answer()


# зтягування ролі з бази даних на прикладі боса
async def is_boss(user_id):
    role, _ = await get_role_and_id(user_id)
    return role == "boss_role"


@router.callback_query(lambda c: c.data == "contact_bos")
async def contact_bos_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    # Перевірка чи користувач є босом
    if await is_boss(user_id):
        await callback_query.message.answer("Оберіть з ким хочете зв'язатися:", reply_markup=kb.keyboard_contact_bos)
    else:
        await callback_query.answer("Ви не маєте доступу до цієї опції.")

    await callback_query.answer()
