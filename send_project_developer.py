from aiogram.fsm.state import State, StatesGroup
class code_developer(StatesGroup):
    file = State()
    command = State()