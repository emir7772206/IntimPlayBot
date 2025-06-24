from aiogram import Bot, Dispatcher, types, executor
import logging, os, random

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

tasks = {
    "❤️ Лёгкий": [
        "Поцелуй в шею… медленно и шёпотом.",
        "Обними сзади и прошепчи желание.",
        "Погладь волосы с чувственностью."
    ],
    "🔥 Контроль": [
        "Прикажи встать на колени и шёпотом проведи рукой.",
        "Завяжи ей глаза шарфом и медленно проведи по телу.",
        "Скажи: «Ляг». Медленно раздевай и наблюдай."
    ],
    "😈 Предел": [
        "Ты — допросчик: свяжи ей руки, спроси тайну плёткой.",
        "Запрети двигаться — ты решаешь время и прикосновения.",
        "Не прикасайся — пусть умоляет."
    ]
}

@dp.message_handler(commands=['start', 'play'])
async def cmd_start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add("❤️ Лёгкий", "🔥 Контроль", "😈 Предел", types.KeyboardButton("/stop"))
    await message.answer("Выбери уровень игры:", reply_markup=kb)

@dp.message_handler(lambda m: m.text in tasks)
async def send_task(message: types.Message):
    task = random.choice(tasks[message.text])
    await message.answer(f"🎲 Задание:\n{task}\n\n👉 /play — ещё, /stop — закончить")

@dp.message_handler(commands=['stop'])
async def cmd_stop(message: types.Message):
    await message.answer("⛔ Игра остановлена. Наслаждайтесь друг другом ❤️")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
