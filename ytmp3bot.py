import os
import telebot
import yt_dlp
from telebot import apihelper
from dotenv import load_dotenv

# Load token dari file .env khusus
load_dotenv("ytmp3bot.env")
TOKEN = os.getenv("TOKEN")

# Validasi token
if not TOKEN:
    print("❌ TOKEN tidak ditemukan di file .env")
    exit(1)

# Inisialisasi bot
bot = telebot.TeleBot(TOKEN)

# Respon /start (kalimat pertama dihapus)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Kirim link YouTube untuk diubah ke MP3.")

# Respon link YouTube
@bot.message_handler(func=lambda message: True)
def download_mp3(message):
    url = message.text
    msg = bot.reply_to(message, "🎧 Sedang mengunduh dan mengubah ke MP3...")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')

        with open(filename, 'rb') as audio:
            bot.send_audio(message.chat.id, audio)

        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, f"❌ Gagal mengunduh: {e}")

# Jalankan bot
if __name__ == "__main__":
    print("🚀 Menjalankan ytmp3bot")
    bot.infinity_polling()
