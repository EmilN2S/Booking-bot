from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    language = State()
    name = State()
    phone = State()
    confirm = State()