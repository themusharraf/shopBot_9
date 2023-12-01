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

keyWen = [
    [types.KeyboardButton(text="Palto 🧥"), types.KeyboardButton(text="Etik 🥾")],
    [types.KeyboardButton(text="Qulqop 🧤"), types.KeyboardButton(text="Sharf 🧣")],
]

wenKey = types.ReplyKeyboardMarkup(keyboard=keyWen, resize_keyboard=True)
