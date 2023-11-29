import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import token
from buttons import keyboard, sezonkey

logging.basicConfig(level=logging.INFO)

TOKEN = token

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f" {message.from_user.first_name} salom sizga qanday yordam ber olman")


@dp.message(Command("shop"))
async def shop(message: Message):
    await message.answer(f" {message.from_user.first_name} shop turini tanlang", reply_markup=keyboard)

    @dp.message(F.text == "Keyimlar")
    async def keyimlar(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/upbBmapdjXNvU1im8", reply_markup=sezonkey)

    @dp.message(F.text == "Texnika")
    async def texnika(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/G72qTPNQBqg8gE257", caption="my shoping")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
