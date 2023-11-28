import types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

keyboard_authentication = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Пройти аутентифікацію",
                             url="https://www.google.com.ua/"),
    ]])

keyboard_role = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Бос ",
                             callback_data="boss_role"),
        InlineKeyboardButton(text = " Дизайнер ",
                             callback_data="designer_role"),
        InlineKeyboardButton(text = " Бухгалтер ",
                             callback_data="accountant_role"),
        InlineKeyboardButton(text = " Розробник ",
                             callback_data="developer_role"),

    ]]
)

keyboard_designer = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Повернутися ",
                            callback_data="back"),
        InlineKeyboardButton(text = " Зв'язатися ",
                            callback_data="contact"),
        InlineKeyboardButton(text = " Надіслати дизайн ",
                             callback_data="send_design"),
        ]]
)


