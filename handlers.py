from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F

from states import User
from keyboard import keyboard_user
from functions import find_combinations


router = Router()

################################################ КНОПКИ ###############################################################


@router.message(F.text == 'Начать ввод параметров сначала')
async def button_press(msg: Message, state: FSMContext):
    """ Начало ввода параметров сначала при нажатии кнопки """
    await state.set_state(User.first_value)
    await msg.answer('Введи первый параметр - КОЛИЧЕСТВО ЗУБОВ ДЕТАЛИ (12 или 16):')


################################################ ХЭНДЛЕРЫ #############################################################


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(User.start_user)
    await msg.answer('Привет! Этот БОТ вычисляет данные для фрейзерного станка.\nНо прежде чем ты начнешь его использовать, тебе необходимо ввести пароль.\n\nВведи пароль:')


@router.message(User.start_user)
async def process_passage_password(msg: Message, state: FSMContext):
    """ Прохождение пароля """
    if msg.text == 'fraser':
        await state.set_state(User.first_value)
        await msg.answer('Введи первый параметр - КОЛИЧЕСТВО ЗУБОВ ДЕТАЛИ (12 или 16):')
    else:
        await msg.answer('Ты ввел неправильный пароль, к сожалению ты не можешь продолжить...')


@router.message(User.first_value)
async def process_first_value(msg: Message, state: FSMContext):
    """ Ввод первого параметра """
    if msg.text.isdigit():
        if int(msg.text) == 12 or int(msg.text) == 16:
            await state.update_data(first_value=int(msg.text))
            await state.set_state(User.second_value)
            await msg.answer('Введи второй параметр - ТОЧНОСТЬ (КОЛИЧЕСТВО ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ) (от 3 до 8):', reply_markup=await keyboard_user())
        else:
            await msg.answer('Ты ввел неправильное значение КОЛИЧЕСТВА ЗУБОВ ДЕТАЛИ.\nЗначение должно равно 12 или 16.\nВведи правильное значение:')
    else:
        await msg.answer('Ты ввел неправильное значение КОЛИЧЕСТВА ЗУБОВ ДЕТАЛИ.\nВведи правильное значение:')


@router.message(User.second_value)
async def process_second_value(msg: Message, state: FSMContext):
    """ Ввод второго параметра """
    if msg.text.isdigit():
        if int(msg.text) in [i for i in range(3, 9)]:
            await state.update_data(second_value=int(msg.text))
            await state.set_state(User.third_value)
            await msg.answer('Введи третий параметр - ПОСТОЯННАЯ ДЕЛИТЕЛЬНАЯ СТАНКА (18 или 24):', reply_markup=await keyboard_user())
        else:
            await msg.answer('Ты ввел неправильное значение ТОЧНОСТИ (КОЛИЧЕСТВО ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ).\nЗначение должно входить в диапазон от 3 до 8.\nВведи правильное значение:')
    else:
        await msg.answer('Ты ввел неправильное значение ТОЧНОСТИ (КОЛИЧЕСТВО ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ).\nВведи правильное значение:')


@router.message(User.third_value)
async def process_third_value(msg: Message, state: FSMContext):
    """ Ввод третьего параметра """
    if msg.text.isdigit():
        if int(msg.text) == 18 or int(msg.text) == 24:
            await state.update_data(third_value=int(msg.text))
            await state.set_state(User.fourth_value)
            await msg.answer('Введи четвертый параметр - КОЛИЧЕСТВО РЕЗУЛЬТАТОВ (от 11 до 100):', reply_markup=await keyboard_user())
        else:
            await msg.answer('Ты ввел неправильное значение ПОСТОЯННОЙ ДЕЛИТЕЛЬНОЙ СТАНКА.\nЗначение может быть равно 18 или 24.\nВведи правильное значение:')
    else:
        await msg.answer('Ты ввел неправильное значение ПОСТОЯННОЙ ДЕЛИТЕЛЬНОЙ СТАНКА.\nВведи правильное значение:')


@router.message(User.fourth_value)
async def process_fourth_value(msg: Message, state: FSMContext):
    """ Ввод четвертого параметра """
    if msg.text.isdigit():
        if int(msg.text) in [i for i in range(11, 101)]:
            data = await state.update_data(fourth_value=int(msg.text))
            shesterni = [24, 25, 30, 30, 45, 46, 47, 48, 50, 50, 54, 55, 55, 55, 57, 59, 60, 60, 62, 64, 69, 72, 72, 80, 85, 90, 92, 95]
            u = data['third_value'] / data['first_value']
            u_rounded = round(u, data['second_value'])
            table_results = find_combinations(shesterni, data['second_value'], u_rounded, data['fourth_value'])
            await msg.answer(f'Результат:', reply_markup=await keyboard_user())
            for row in table_results:
                await msg.answer(f'A={row[0]}, B={row[1]}, C={row[2]}, D={row[3]}')
        else:
            await msg.answer('Ты ввел неправильное значение КОЛИЧЕСТВА РЕЗУЛЬТАТОВ.\nЗначение должно входить в диапазон от 11 до 101.\nВведи правильное значение:')
    else:
        await msg.answer('Ты ввел неправильное значение КОЛИЧЕСТВА РЕЗУЛЬТАТОВ.\nВведи правильное значение:')



#print(await state.storage.get_state(state.key))  просмотреть состояние стейт машины
