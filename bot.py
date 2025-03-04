import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import executor

# Твой токен бота (лучше хранить в переменных окружения)
TOKEN = "ТВОЙ_ТОКЕН_БОТА"

# Логирование
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [KeyboardButton("📅 Заполнить дневник"), KeyboardButton("🎯 Цели"), KeyboardButton("🏋️ Спорт")]
keyboard.add(*buttons)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой коуч-бот по саморазвитию. Чем займемся сегодня?", reply_markup=keyboard)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
