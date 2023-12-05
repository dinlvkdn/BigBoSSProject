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



# BOS
keyboard_boss = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Зареєструвати проект ",
                            callback_data="send_project_bos"),
        InlineKeyboardButton(text = " Змінити проект ",
                             callback_data="change_project_bos"),
        InlineKeyboardButton(text = " Зв'язатися ",
                            callback_data="contact_bos"),
        InlineKeyboardButton(text = " Повернути проект ",
                            callback_data="back_project_bos"),
        ]]
)

keyboard_contact_bos = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Бухгалтер ",
                            callback_data="accountant_contact_bos"),
        InlineKeyboardButton(text = " Дизайнер ",
                             callback_data="designer_contact_bos"),
        InlineKeyboardButton(text = " Розробник ",
                            callback_data="developer_contact_bos"),
        InlineKeyboardButton(text = " Повернутися назад ",
                            callback_data="back_contact_bos"),
        ]]
)

# DESIGNER
keyboard_designer = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Повернути ",
                            callback_data="back"),
        InlineKeyboardButton(text = " Зв'язатися ",
                            callback_data="contact"),
        InlineKeyboardButton(text = " Надіслати дизайн ",
                             callback_data="send_design"),
        ]]
)

keyboard_contact_designer = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Бос ",
                             callback_data="bos_contact_designer"),
        InlineKeyboardButton(text = " Бухгалтер ",
                            callback_data="accountant_contact_designer"),
        InlineKeyboardButton(text = " Розробник ",
                            callback_data="developer_contact_designer"),
        InlineKeyboardButton(text = " Повернутися назад ",
                            callback_data="back_contact_designer"),
        ]]
)




# зв'язок для дизайнера
contact_keyboard_designer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Бос", callback_data="boss"),
            InlineKeyboardButton(text="Бухгалтер", callback_data="accountant"),
            InlineKeyboardButton(text="Розробник", callback_data="developer"),
        ],
        [InlineKeyboardButton(text="Повернутися назад", callback_data="back")],
    ]
)


