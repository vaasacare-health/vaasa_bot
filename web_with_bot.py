# at top
import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "OK"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

# Start your bot polling in a background thread
def start_bot():
    # replace below with how you start polling now
    # e.g. bot.infinity_polling() or bot.polling(none_stop=True)
    from vaasa_bot import start_polling   # if you refactor
    start_polling()

if __name__ == "__main__":
    # start web + bot threads
    Thread(target=run_web).start()
    Thread(target=start_bot).start()