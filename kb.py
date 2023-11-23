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

