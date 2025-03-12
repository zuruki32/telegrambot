import asyncio
from aiogram import Bot, Dispatcher, types

import os
TOKEN = os.getenv("BOT_TOKEN")  # دریافت توکن از Railway

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ✅ هندلر برای /start
@dp.message(commands=['start'])
async def start_command(message: types.Message):
    user_name = message.from_user.first_name  # دریافت نام کاربر
    await message.answer(f"سلام {user_name}! 👋\n به ربات چنل آیریسکای خوش اومدی!جیگر طلا! 🤖")

# ✅ هندلر برای دریافت و تکرار پیام‌های معمولی
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"📩 پیامت دریافت شد قند عسل در اسرع وقت میخونیمش: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
