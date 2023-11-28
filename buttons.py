from aiogram import types

key = [
    [types.KeyboardButton(text="Keyimlar", ), types.KeyboardButton(text="Texnika", )],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)
