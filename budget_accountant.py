from aiogram.fsm.state import State, StatesGroup
class send_budget_accountant(StatesGroup):
    budget = State()
    command = State()