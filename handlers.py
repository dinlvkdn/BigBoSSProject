import sqlite
from aiogram import F, Router,Bot, Dispatcher, types
from aiogram.client import bot
from aiogram.types import Message
from aiogram.filters import Command
import kb
import text
from sqlite import db_start, create_profile, edit_profile, get_role_and_id

API_TOKEN = '6942412160:AAE9DtY6ic3viZPrg35qvm1Klwi_MZ9B2S0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

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
    # Записали роль в базу даних
    await create_profile(user_id, role=selected_role)
    role = await get_role_and_id(user_id)

    if role == "boss_role":
        await callback_query.message.answer_sticker(sticker=text.bos_sticker)
        await callback_query.answer(text=text.role_bos)
        await callback_query.message.answer("Бос, оберіть опцію:", reply_markup=kb.keyboard_boss)

    elif role == "accountant_role":
        await callback_query.message.answer_sticker(sticker=text.acc_sticker)
        await callback_query.answer(text="Ви обрали роль - Бухгалтер")
        await callback_query.message.answer("Бухгалтер, оберіть опцію:", reply_markup=kb.keyboard_accountant)


    elif role == "designer_role":
        await callback_query.message.answer_sticker(sticker=text.des_sticker)
        await callback_query.answer(text="Ви обрали роль - Дизайнер")
        await callback_query.message.answer("Дизайнер, оберіть опцію:", reply_markup=kb.keyboard_designer)

    elif role == "developer_role":
        await callback_query.message.answer_sticker(sticker=text.dev_sticker)
        await callback_query.answer(text="Ви обрали роль - Розробник")

    await callback_query.answer()


# зтягування ролі з бази даних на прикладі боса
async def is_boss(user_id):
    role = await get_role_and_id(user_id)
    return role == "boss_role"


async def is_designer(user_id):
    role = await get_role_and_id(user_id)
    return role == "designer_role"


async def is_accountant(user_id):
    role = await get_role_and_id(user_id)
    return role == "accountant_role"


async def is_developer(user_id):
    role = await get_role_and_id(user_id)
    return role == "developer_role"


@router.callback_query(lambda c: c.data == "contact_bos")
async def contact_bos_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    # Перевірка чи користувач є босом
    if await is_boss(user_id):
        await callback_query.message.answer("Оберіть з ким хочете зв'язатися:", reply_markup=kb.keyboard_contact_bos)
    else:
        await callback_query.answer("Ви не маєте доступу до цієї опції.")

    await callback_query.answer()


@router.callback_query(lambda c: c.data == "send_project_bos")
async def send_project_bos_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    # Перевірка чи користувач є босом
    if await is_boss(user_id):
        await callback_query.message.answer("Ми готові прийняти твій проект! Будь ласка, надішли файл проекту. Також можна надіслати посилання на проект. Ми завжди готові до нових викликів! ", reply_markup=kb.keyboard_send_project_bos)
    else:
        await callback_query.answer("Ви не маєте доступу до цієї опції.")

    await callback_query.answer()


@router.message(F.document)
async def handle_received_file(message: types.Message):
    accountant_user_id = await sqlite.get_user_id_by_role("accountant_role")
    file_id = message.document.file_id
    caption = message.caption
    if accountant_user_id:
        await bot.send_document(chat_id=accountant_user_id, document=file_id, caption=caption)
        await message.reply(text='Файл успішно надіслано бухгалтеру')


@router.callback_query(lambda c: c.data == "return")
async def return_to_role_selection(callback_query: types.CallbackQuery):

    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_role)


@router.callback_query(lambda c: c.data == "back_contact_designer")
async def return_to_keyboard_designer(callback_query: types.CallbackQuery):

    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_designer)

@router.callback_query(lambda c: c.data == "back_contact_bos")
async def return_to_keyboard_bos(callback_query: types.CallbackQuery):

    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_boss)


@router.callback_query(lambda c: c.data == "contact_accountant")
async def return_to_keyboard_bos(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.message.answer("Оберіть з ким хочете зв'язатися:", reply_markup=kb.keyboard_contact_accountant)

    await callback_query.answer()

@router.callback_query(lambda c: c.data.startswith("designer_contact_accountant"))
async def contact_designer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.answer("Напишіть повідомлення до дизайнера.")

@router.callback_query(lambda c: c.data.startswith("bos_contact_accountant"))
async def contact_bos(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.answer("Напишіть повідомлення до боса.")

@router.callback_query(lambda c: c.data.startswith("developer_contact_accountant"))
async def contact_developer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.answer("Напишіть повідомлення до розробника.")

@router.callback_query(lambda c: c.data == "back_contact_accountant")
async def return_to_keyboard_bos(callback_query: types.CallbackQuery):

    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_accountant)
