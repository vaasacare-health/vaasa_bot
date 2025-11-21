import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome to VAASA School Health Bot!")

@bot.message_handler(func=lambda m: True)
def reply_all(message):
    bot.reply_to(message, "I received your message!")

bot.infinity_polling()