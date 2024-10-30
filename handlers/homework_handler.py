from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states.homework_states import HomeworkStates
from database.db import save_homework

GROUPS = ["Python 47-01", "Python 47-02"
          "Python 48-01", "Python 48-02"]

async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*[KeyboardButton(group) for group in GROUPS])
    await message.answer("Выберите вашу группу:", reply_markup=markup)
    await HomeworkStates.waiting_for_group.set()

async def group_handler(message: types.Message, state: FSMContext):
    if message.text not in GROUPS:
        await message.answer("Пожалуйста, выберите группу из списка.")
        return
    await state.update_data(group_name=message.text)
    await message.answer("Введите номер домашнего задания (от 1 до 8):")
    await HomeworkStates.waiting_for_homework_number.set()

async def homework_number_handler(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or not (1 <= int(message.text) <= 8):
        await message.answer("Пожалуйста, введите число от 1 до 8.")
        return
    await state.update_data(homework_number=int(message.text))
    await message.answer("Отправьте ссылку на ваш GitHub репозиторий:")
    await HomeworkStates.waiting_for_github_link.set()

async def github_link_handler(message: types.Message, state: FSMContext):
    if not message.text.startswith("https://github.com"):
        await message.answer("Ссылка должна начинаться с 'https://github.com'")
        return
    await state.update_data(github_link=message.text)
    data = await state.get_data()
    save_homework(data['name'], data['group_name'], data['homework_number'], data['github_link'])
    await message.answer("Спасибо! Ваше домашнее задание сохранено.")
    await state.finish()

def register_handlers_homework(dp: Dispatcher):
    dp.register_message_handler(name_handler, state=HomeworkStates.waiting_for_name)
    dp.register_message_handler(group_handler, state=HomeworkStates.waiting_for_group)
    dp.register_message_handler(homework_number_handler, state=HomeworkStates.waiting_for_homework_number)
    dp.register_message_handler(github_link_handler, state=HomeworkStates.waiting_for_github_link)
