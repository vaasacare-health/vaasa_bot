# minimal telegram bot using pyTelegramBotAPI
import telebot

# <<-- Put your bot token (between the quotes) on a single line here:
BOT_TOKEN = "8252983187:AAEpQErz8JWBm_GOLq9YjP RTFI8wl7B3j5E"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am VAASA Assistant. How can I help you?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + (message.text or ""))

print("Bot running...")
bot.infinity_polling()