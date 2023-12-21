from aiogram.fsm.state import State, StatesGroup
class get_message_from_bos(StatesGroup):
    message = State()
    command = State()