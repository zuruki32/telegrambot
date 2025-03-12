import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command  # ✅ اضافه کردن فیلتر Command

import os
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()  # ✅ ایجاد دیسپچر جدید

# ✅ هندلر جدید برای /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"سلام {user_name}! 👋\nبه ربات ما خوش آمدی! 🤖")

# ✅ هندلر جدید برای پیام‌های معمولی
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"📩 پیامت دریافت شد: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())