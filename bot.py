import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ✅ تنظیمات لاگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")
ADMINS = [5487434442]

if not TOKEN:
    raise ValueError("❌ توکن یافت نشد! لطفا BOT_TOKEN را تنظیم کنید.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ✅ هندلر استارت
@dp.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"سلام {user_name}! 👋\nبه ربات ما خوش آمدی!")

# ✅ هندلر فوروارد
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
                logger.info(f"✅ پیام به ادمین {admin_id} ارسال شد")
            except Exception as e:
                logger.error(f"🔥 خطا در ارسال به ادمین: {str(e)}")

# ✅ تابع اصلی با مدیریت خطا
async def main():
    try:
        logger.info("🚀 ربات در حال راه‌اندازی...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"⛔ خطای بحرانی: {str(e)}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())