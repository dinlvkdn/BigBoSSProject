import types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

keyboard_authentication = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Пройти аутентифікацію",
                             url="https://www.google.com.ua/"),
    ]])

