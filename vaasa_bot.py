import telebot
from flask import Flask, request

TOKEN = "YOUR_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! VAASA bot is active.")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://YOUR_RENDER_URL/" + TOKEN)
    return "Webhook set", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)