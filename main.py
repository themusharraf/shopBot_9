import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import token
from buttons import keyboard, sezonkey, wenKey
from shopkey import key, shopKey

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

        @dp.message(F.text == "Qish 🥶")
        async def keyimlar(message: Message):
            await message.answer_photo(photo="https://images.app.goo.gl/2JjuhuBUpqTmNdJq8", reply_markup=wenKey)

            @dp.message(F.text == "Palto 🧥")
            async def keyimlar(message: Message):
                await message.answer_photo(photo="https://images.app.goo.gl/LxHrLfZFvyZbGSZw6", caption="""Camel Klasik Palto
500 USD 💵
Manken Ölçüleri: 50/M Boy: 188 cm
Göğüs: 98 cm Bel: 85 cm Basen: 99 cm
""",
                                           reply_markup=shopKey.as_markup())

    @dp.message(F.text == "Texnika")
    async def texnika(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/G72qTPNQBqg8gE257", caption="my shoping",
                                   reply_markup=key.as_markup())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
