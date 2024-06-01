from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    start_user = State()
    first_value = State()
    second_value = State()
    third_value = State()
    fourth_value = State()
