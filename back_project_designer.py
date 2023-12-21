from aiogram.fsm.state import State, StatesGroup
class get_message_from_designer(StatesGroup):
    message = State()
    command = State()