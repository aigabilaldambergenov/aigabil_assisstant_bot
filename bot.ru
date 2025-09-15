from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "Мұнда_сіздің_бот_токеніңізді_қойыңыз"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Сәлем! Мен сенің оң қолыңмын 🤖")

def start_bot():
    executor.start_polling(dp, skip_updates=True)