import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Вставьте сюда НОВЫЙ токен от BotFather
TOKEN = "8335931640:AAG3k7-f3d38aced490nm5RPGmNrvdRr-hY"

# Правильная ссылка на вашу игру
GAME_URL = "https://jonibekiumedzod0770-wq.github.io/gamehub/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КЛАВИАТУРЫ ---

def get_main_keyboard():
    buttons = [
        [
            types.KeyboardButton(text="🎮 Играть"),
            types.KeyboardButton(text="ℹ️ О нас")
        ],
        [
            types.KeyboardButton(text="📞 Контакты")
        ]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_game_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Открыть игры", web_app=WebAppInfo(url=GAME_URL))]
    ])

# --- ОБРАБОТЧИКИ КОМАНД ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в GameHub Bot!\n"
        "Здесь ты можешь играть в лучшие игры бесплатно.",
        reply_markup=get_main_keyboard()
    )

@dp.message(F.text == "🎮 Играть")
async def cmd_play(message: types.Message):
    # Теперь здесь используется правильная ссылка GAME_URL
    await message.answer(
        "Нажми кнопку ниже, чтобы начать играть:",
        reply_markup=get_game_keyboard()
    )

@dp.message(F.text == "ℹ️ О нас")
async def cmd_about(message: types.Message):
    await message.answer("GameHub — это платформа с бесплатными браузерными играми. Мы сделали Тетрис, Змейку, Гонки и Сапера!")

@dp.message(F.text == "📞 Контакты")
async def cmd_contacts(message: types.Message):
    await message.answer("По всем вопросам пишите: @ваш_юзернейм")

# --- ЗАПУСК ---

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")