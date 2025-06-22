import os
from dotenv import load_dotenv

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'ytmp3bot.env')
load_dotenv(dotenv_path=dotenv_path)

# Ambil variabel dari .env
TELEGRAM_BOT_TOKEN = os.getenv("TOKEN")

# Validasi isi variabel (optional tapi sangat disarankan)
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN tidak ditemukan ytmp3bot.env")
