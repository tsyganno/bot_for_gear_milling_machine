from aiogram import types


async def keyboard_user():
    """ Кнопка для перехода в начало ввода параметров """
    kb = [
        [types.KeyboardButton(text='Начать ввод параметров сначала')],
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return markup
