import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

# Твой токен бота
TOKEN = os.getenv("TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)  

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [KeyboardButton("🎯 Цели"), KeyboardButton("⚽ Спорт")]
keyboard.add(*buttons)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой коуч по саморазвитию. Чем займемся сегодня?", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
