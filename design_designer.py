from aiogram.fsm.state import State, StatesGroup
class design_designer(StatesGroup):
    file = State()
    command = State()