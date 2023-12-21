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
        InlineKeyboardButton(text = " Роль ",
                            callback_data="return"),
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


kb_sendPr = [[KeyboardButton(text="Надіслати файл")]]

keyboard_send_project_bos = ReplyKeyboardMarkup(keyboard=kb_sendPr, resize_keyboard=True)
kb_sendText = [[KeyboardButton(text="Надіслати повідомлення")]]
kb_send_mess_from_acc_to_desi = ReplyKeyboardMarkup(keyboard = kb_sendText, resize_keyboard=True)

# DESIGNER
keyboard_designer = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Повернути ",
                            callback_data="back_project_designer"),
        InlineKeyboardButton(text = " Зв'язатися ",
                            callback_data="contact"),
        InlineKeyboardButton(text = " Надіслати дизайн ",
                             callback_data="send_design"),
        InlineKeyboardButton(text = " Роль ",
                            callback_data="return"),
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


# accountant
keyboard_accountant = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Повернути ",
                            callback_data="back_project_accountant"),
        InlineKeyboardButton(text = " Зв'язатися ",
                            callback_data="contact_accountant"),
        InlineKeyboardButton(text = " Підтвердити ",
                             callback_data="confirm_budget_accountant"),
        InlineKeyboardButton(text = " Роль ",
                            callback_data="return"),
        ]]
)

keyboard_contact_accountant = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Бос ",
                             callback_data="bos_contact_accountant"),
        InlineKeyboardButton(text = " Дизайнер ",
                            callback_data="designer_contact_accountant"),
        InlineKeyboardButton(text = " Розробник ",
                            callback_data="developer_contact_accountant"),
        InlineKeyboardButton(text = " Повернутися назад ",
                            callback_data="back_contact_accountant"),
        ]]
)


# Developer
keyboard_developer= InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Повернути ",
                            callback_data="back_project_developer"),
        InlineKeyboardButton(text = " Зв'язатися ",
                            callback_data="contact_developer"),
        InlineKeyboardButton(text = " Підтвердити ",
                             callback_data="confirm_design_developer"),
        InlineKeyboardButton(text = " Роль ",
                            callback_data="return"),
        ]]
)

keyboard_contact_developer = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text = " Бос ",
                             callback_data="bos_contact_developer"),
        InlineKeyboardButton(text = " Дизайнер ",
                            callback_data="designer_contact_developer"),
        InlineKeyboardButton(text = " Бухгалтер ",
                            callback_data="accountant_contact_developer"),
        InlineKeyboardButton(text = " Повернутися назад ",
                            callback_data="back_contact_developer"),
        ]]
)