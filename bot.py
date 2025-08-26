from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("8219038004:AAEjESODgI_olGYUG85cs293LC9bUv7AfJE")  # Render ichida sozlanadi

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Salom! Bot ishlayapti ✅")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)