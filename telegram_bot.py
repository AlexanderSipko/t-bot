# telegram_bot.py
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from dotenv import load_dotenv, dotenv_values
import os

# Загрузка переменных окружения из файла .env_
load_dotenv() 
config = dotenv_values(".env") 

# Получение токена бота
TOKEN = config.get('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [
        ['Проверить счет'],  # Кнопка для проверки счета
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    if update.message:  # Проверяем, что сообщение существует
        await update.message.reply_text(
            f'Привет, {user.first_name}! Я тестовый бот для проверки счета.\n'
            'Чтобы проверить свой счет, нажмите кнопку "Проверить счет".',
            reply_markup=reply_markup
        )

async def check_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    balance = random.randint(0, 1000)  # Генерация случайного значения счета
    if update.message:  # Проверяем, что сообщение существует
        await update.message.reply_text(f'Ваш текущий счет: {balance} рублей.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text == 'Проверить счет':  # Проверяем, что сообщение существует
        await check_balance(update, context)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Обработка текстовых сообщений
    
    application.run_polling()

if __name__ == '__main__': 
    main()