# vaasa_bot.py
# Minimal Telegram bot using pyTelegramBotAPI

import os
import sys
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN environment variable is not set. Exiting.")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am Vaasa School Health assistant. How can I help you?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text or ""
    bot.reply_to(message, "You said: " + text)

print("Bot running...")
# recommended polling
bot.infinity_polling()