import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")
ADMINS = [5487434442]  # 🔴 آیدی عددی ادمین‌ها را اینجا وارد کنید

if not TOKEN:
    raise ValueError("❌ توکن یافت نشد! لطفا BOT_TOKEN را تنظیم کنید.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ✅ هندلر /start برای کاربران معمولی
@dp.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"سلام {user_name}! 👋\nبه ربات چنل آیریسکای خوش اومدی! جیگر طلا! 🤖")

# ✅ هندلر فوروارد پیام به ادمین‌ها
@dp.message()
async def forward_to_admins(message: types.Message):
    if message.from_user.id not in ADMINS:
        for admin_id in ADMINS:
            try:
                await bot.forward_message(
                    chat_id=admin_id,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id
                )
                print(f"✅ پیام با موفقیت به آیدی {admin_id} ارسال شد")  # لاگ موفقیت
            except Exception as e:
                print(f"🔥 خطا در ارسال به آیدی {admin_id}: {str(e)}")  # لاگ خطا

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())