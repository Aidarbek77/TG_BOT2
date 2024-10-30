from aiogram.dispatcher.filters.state import State, StatesGroup

class HomeworkStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_group = State()
    waiting_for_homework_number = State()
    waiting_for_github_link = State()
