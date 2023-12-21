from aiogram.fsm.state import State, StatesGroup
class ContactDeveloper(StatesGroup):
    textD = State()
    typeD = State()