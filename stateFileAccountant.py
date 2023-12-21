from aiogram.fsm.state import State, StatesGroup
class getFileAccountant(StatesGroup):
    file = State()
    type = State()