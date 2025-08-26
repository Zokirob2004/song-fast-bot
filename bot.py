from aiogram import Bot, Dispatcher, executor, types
import yt_dlp
import os

TOKEN = os.getenv("8219038004:AAEjESODgI_olGYUG85cs293LC9bUv7AfJE")  # Render environmentdan oladi
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Salom! Menga qo‘shiq nomini yozing 🎵")

@dp.message_handler()
async def search_song(message: types.Message):
    query = message.text
    await message.reply(f"🔎 Qidirilmoqda: {query}")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'outtmpl': 'song.%(ext)s',
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            file_name = ydl.prepare_filename(info['entries'][0])

        await message.reply_audio(open(file_name, 'rb'))
        os.remove(file_name)

    except Exception as e:
        await message.reply("❌ Qo‘shiq topilmadi.")

if name == "main":
    executor.start_polling(dp, skip_updates=True)