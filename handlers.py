from aiogram.fsm.context import FSMContext
from stateFile import getFile
from stateText import Contact

import db
import sqlite
from aiogram import F, Router, Bot, Dispatcher, types
from aiogram.client import bot
from aiogram.types import Message
from aiogram.filters import Command
import kb
import text
from sqlite import db_start, create_profile, is_role_taken, get_role_and_id

API_TOKEN = '6942412160:AAE9DtY6ic3viZPrg35qvm1Klwi_MZ9B2S0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

file_temp = 0
caption_temp = 0


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
    if await is_role_taken(selected_role):
        await callback_query.answer(text=f"Роль {selected_role} вже зайнята.")
        return
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
        await callback_query.message.answer("Розробник, оберіть опцію:", reply_markup=kb.keyboard_developer)

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

#  ЗВ'ЯЗОК
@router.callback_query(lambda c: c.data == "contact_bos")
async def contact_bos_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    # Перевірка чи користувач є босом
    if await is_boss(user_id):
        await callback_query.message.answer("Оберіть з ким хочете зв'язатися:", reply_markup=kb.keyboard_contact_bos)
    else:
        await callback_query.answer("Ви не маєте доступу до цієї опції.")

    await callback_query.answer()



@router.callback_query(lambda c: c.data in {"accountant_contact_bos", "designer_contact_bos", "developer_contact_bos"})
async def send_message_bos(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(text=f'Бос, напишіть повідомлення ')

    await state.set_state(Contact.text)
    await state.set_data(dict(user_type=callback_query.data))
    await callback_query.answer()


@router.message(Contact.text)
async def get_message_bos(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    user_type = data.get('user_type')
    accountant = await sqlite.get_user_id_by_role("accountant_role")
    designer = await sqlite.get_user_id_by_role("designer_role")
    developer = await sqlite.get_user_id_by_role("developer_role")
    if(user_type == "accountant_contact_bos"):
        await bot.send_animation(chat_id=accountant, animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=accountant, text=f"У вас нове повідомлення від боса:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')
    elif (user_type == "designer_contact_bos"):
        await bot.send_animation(chat_id=designer,
                                 animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=designer, text=f"У вас нове повідомлення від боса:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')
    elif (user_type == "developer_contact_bos"):
        await bot.send_animation(chat_id=developer,
                                 animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=developer, text=f"У вас нове повідомлення від боса:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')

    await state.clear()


@router.callback_query(lambda c: c.data == "contact_accountant")
async def contact_accountant(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.message.answer("Оберіть з ким хочете зв'язатися:", reply_markup=kb.keyboard_contact_accountant)

    await callback_query.answer()


@router.callback_query(lambda c: c.data in {"bos_contact_accountant", "designer_contact_accountant", "developer_contact_accountant",
                         "back_contact_accountant"})
async def send_message_accountant(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(text=f'Бухгалтер, напишіть повідомлення: ')

    await state.set_state(Contact.text)
    await state.set_data(dict(user_type=callback_query.data))
    await callback_query.answer()


@router.message(Contact.text)
async def get_message_accountant(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    user_type = data.get('user_type')
    bos = await sqlite.get_user_id_by_role("boss_role")
    designer = await sqlite.get_user_id_by_role("designer_role")
    developer = await sqlite.get_user_id_by_role("developer_role")
    if(user_type == "bos_contact_accountant"):
        await bot.send_animation(chat_id=bos, animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=bos, text=f"У вас нове повідомлення від бухгалтера:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')
    elif (user_type == "designer_contact_accountant"):
        await bot.send_animation(chat_id=designer,
                                 animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=designer, text=f"У вас нове повідомлення від бухгалтера:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')
    elif (user_type == "developer_contact_accountant"):
        await bot.send_animation(chat_id=developer,
                                 animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=developer, text=f"У вас нове повідомлення від бухгалтера:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')

    await state.clear()


@router.callback_query(lambda c: c.data == "contact_developer")
async def contact_developer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await callback_query.message.answer("Оберіть з ким хочете зв'язатися:", reply_markup=kb.keyboard_contact_developer)

    await callback_query.answer()


@router.callback_query(lambda c: c.data in {"bos_contact_developer", "designer_contact_developer", "accountant_contact_developer"})
async def send_message_developer(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(text=f'Робробник, напишіть повідомлення: ')

    await state.set_state(Contact.text)
    await state.set_data(dict(user_type=callback_query.data))
    await callback_query.answer()


@router.message(Contact.text)
async def get_message_developer(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    user_type = data.get('user_type')
    bos = await sqlite.get_user_id_by_role("boss_role")
    designer = await sqlite.get_user_id_by_role("designer_role")
    accountant = await sqlite.get_user_id_by_role("accountant_role")
    if(user_type == "bos_contact_developer"):
        await bot.send_animation(chat_id=bos, animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=bos, text=f"У вас нове повідомлення від розробника:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')
    elif (user_type == "designer_contact_developer"):
        await bot.send_animation(chat_id=designer,
                                 animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=designer, text=f"У вас нове повідомлення від розробника:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')
    elif (user_type == "accountant_contact_developer"):
        await bot.send_animation(chat_id=accountant,
                                 animation="CAACAgEAAxkBAAEK-RdlfLNndKTAjloZjVmhM1GXR9y_9AACTQIAAtzQQESgDBKpHPSHsTME")
        await bot.send_message(chat_id=accountant, text=f"У вас нове повідомлення від розробника:\n\n{text}")
        await message.reply(text=f'Повідомлення успішно надіслано.')



    await state.clear()



# @router.callback_query(lambda c: c.data == "send_project_bos")
# async def send_project_bos_callback_handler(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#
#     # Перевірка чи користувач є босом
#     if await is_boss(user_id):
#         await callback_query.message.answer(
#             "📍Ми готові прийняти твій проект!\n Будь ласка, надішли файл проекту.\n Також можна підкріпити коментарі.",
#             reply_markup=kb.keyboard_send_project_bos)
#     else:
#         await callback_query.answer("Ви не маєте доступу до цієї опції.")
#
#     await callback_query.answer()
#
#
# @router.message(F.document)
# async def handle_received_file(message: types.Message):
#     accountant_user_id = await sqlite.get_user_id_by_role("accountant_role")
#     file_id = message.document.file_id
#     caption = message.caption
#     if accountant_user_id:
#         await bot.send_message(chat_id=accountant_user_id,
#                                text="Бос зареєстрував новий проект.\n Будь ласка, перегляньте та оцініть проект щодо бюджету та надайте згоду")
#         await bot.send_document(chat_id=accountant_user_id, document=file_id, caption=caption)
#         await message.reply(text='Файл успішно надіслано бухгалтеру')


@router.callback_query(lambda c: c.data == "return")
async def return_to_role_selection(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_role)


@router.callback_query(lambda c: c.data == "back_contact_designer")
async def return_to_keyboard_designer(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_designer)


@router.callback_query(lambda c: c.data == "back_contact_bos")
async def return_to_keyboard_bos(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_boss)

@router.callback_query(lambda c: c.data == "back_contact_developer")
async def return_to_keyboard_developer(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text.role, reply_markup=kb.keyboard_developer)







# Обробили команду Зареєструвати проект для Боса
@router.callback_query(lambda c: c.data == "send_project_bos")
async def send_project_bos_callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id

    # Перевірка чи користувач є босом
    if await is_boss(user_id):
        await callback_query.message.answer(
            "📍Ми готові прийняти твій проект!\n Будь ласка, надішли файл проекту.\n Також можна підкріпити коментарі.")
    else:
        await callback_query.answer("Ви не маєте доступу до цієї опції.")

    await state.set_state(getFile.file)
    await state.set_data(dict(comand_get_file=callback_query.data))
    await callback_query.answer()


@router.message(getFile.file)
async def handle_received_file(message: types.Message, state: FSMContext):
    accountant_user_id = await sqlite.get_user_id_by_role("accountant_role")
    file_id = message.document.file_id
    caption = message.caption
    data = await state.get_data()
    comand_get_file = data.get('comand_get_file')
    if comand_get_file == 'send_project_bos':
        if accountant_user_id:
            await db.db_start()
            await db.save_file_id(file_id, caption)
            await bot.send_message(chat_id=accountant_user_id,
                                   text="Бос зареєстрував новий проект.\n Будь ласка, перегляньте та оцініть проект щодо бюджету та надайте згоду")
            await bot.send_document(chat_id=accountant_user_id, document=file_id, caption=caption)
            await message.reply(text='Файл успішно надіслано бухгалтеру')
            # await bot.send_message(chat_id=accountant_user_id, reply_markup=kb.)

    await state.clear()


# @router.callback_query(lambda c: c.data == "confirm_budget_accountant")
# async def confirm_budget_accountant(callback_query: types.CallbackQuery):
#     designer_user_id = await sqlite.get_user_id_by_role("designer_role")
#     file_id = await db.get_file_ids()
#     caption = await db.get_captions()
#     if designer_user_id:
#         await bot.send_message(chat_id=designer_user_id,
#                                text="Бос зареєстрував новий проект.\n Бухгалтер підтвердив вже проект, намалюй дизайн і все буде добре")
#         await bot.send_document(chat_id=designer_user_id, document=file_id, caption=caption)
#         await callback_query.message.answer(text="Проект було надіслано дизайнеру")
