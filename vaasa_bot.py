import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN env var is missing")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am VAASA Assistant 🤖")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + (message.text or ""))

if __name__ == "__main__":
    print("Bot running...")
    bot.infinity_polling()