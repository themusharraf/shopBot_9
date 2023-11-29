from aiogram import types

key = [
    [types.KeyboardButton(text="Keyimlar", ), types.KeyboardButton(text="Texnika", )],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)

sezon = [
    [types.KeyboardButton(text="Qish 🥶"), types.KeyboardButton(text="Bahor 🍀")],
    [types.KeyboardButton(text="Kuz 🍁"), types.KeyboardButton(text="Yoz 😎")],
]
sezonkey = types.ReplyKeyboardMarkup(keyboard=sezon, resize_keyboard=True)
