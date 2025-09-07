import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
from bot import register_handlers

# 🔑 Сіздің токеніңіз
API_TOKEN = "7888734931:AAENeWdqsJXU9uqE45_zM2Jt916EHYSTCEk"

# Webhook параметрлері
WEBHOOK_HOST = "https://aigabil-assisstant-bot.up.railway.app"
WEBHOOK_PATH = "/webhook/" + API_TOKEN
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Сервер параметрлері
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = 8080

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Хэндлерлерді тіркеу
register_handlers(dp)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    print("Бот іске қосылды ✅")

async def on_shutdown(dp):
    await bot.delete_webhook()
    print("Бот тоқтады ❌")

if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )