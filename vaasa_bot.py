import telebot
import os

# Load bot token from Render environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am VAASA Assistant 🤖")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    text = message.text or ""
    bot.reply_to(message, "You said: " + text)

print("Bot running...")
bot.infinity_polling()