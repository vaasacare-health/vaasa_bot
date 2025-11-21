import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am VAASA Assistant 🤖")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + (message.text or ""))

print("Bot running...")
bot.infinity_polling()