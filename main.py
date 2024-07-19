from aiogram import types, F, Bot, Dispatcher, filters
import asyncio
import wikipedia


bot = Bot(token="7389084923:AAGSV2ywgwM2-oPYgrCmGz7eVrCylwPscZQ")
dp = Dispatcher(bot=bot)
wikipedia.set_lang("uz")


@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.first_name}, nima boyicha yoki kim boyicha ma'lumot izlayapsiz?")


@dp.message(F.text)
async def wiki(message: types.Message):
    text = wikipedia.summary(message.text)
    await message.answer(text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())