from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

key = InlineKeyboardBuilder()
key.row(types.InlineKeyboardButton(
    text="Apple", url="https://www.apple.com/")
)
key.row(types.InlineKeyboardButton(
    text="Aiogram",
    url="https://docs.aiogram.dev/en/latest/")
)

shopKey = InlineKeyboardBuilder()
shopKey.row(types.InlineKeyboardButton(
    text="Camel Classic XL Palto", url="https://www.kigili.com/kahverengi-klasik-palto-8682607533901/?integration_patern=CAMEL-R&integration_beden=54"
))
