# web_with_bot.py
import os
from threading import Thread
from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN env var is missing")

# --- Telegram bot (long-polling) ---
def start(update, context):
    update.message.reply_text("Hello! I am VAASA Assistant 🤖")

def echo(update, context):
    update.message.reply_text(f"You said: {update.message.text}")

def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

# --- tiny web server to bind to $PORT ---
app = Flask(__name__)

@app.route("/")
def index():
    return "VAASA Bot is running", 200

if __name__ == "__main__":
    # run the bot in a separate thread
    t = Thread(target=run_bot, daemon=True)
    t.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)