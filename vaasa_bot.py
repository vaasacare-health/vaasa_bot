# vaasa_bot.py
# minimal telegram bot using pyTelegramBotAPI (safe: token read from env)

import os
import logging
import telebot
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("BOT_TOKEN environment variable is not set. Exiting.")
    raise RuntimeError("BOT_TOKEN environment variable is not set. Add it to Render environment variables.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am VAASA Assistant. How can I help you?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text or ""
    bot.reply_to(message, "You said: " + text)

if __name__ == "__main__":
    try:
        logger.info("Bot starting (long polling)...")
        # This will loop forever. Render will keep the process running.
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        logger.exception("Exception in bot: %s", e)
        # sleep to avoid crash loops
        time.sleep(5)
        raise