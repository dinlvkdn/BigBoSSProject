from aiogram.fsm.state import State, StatesGroup
class ContactDesigner(StatesGroup):
    textD = State()
    typeD = State()