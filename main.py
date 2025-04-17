from flask import Flask, render_template, request
from chatbot import ChatBot
from datetime import datetime

app = Flask(__name__)
bot = ChatBot()

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("message")
        user_time = datetime.now().strftime("%H:%M:%S")
        bot_response = bot.respond(user_input)
        bot_time = datetime.now().strftime("%H:%M:%S")

        chat_history.append({
            "sender": "You",
            "message": user_input,
            "time": user_time
        })
        chat_history.append({
            "sender": "Bot",
            "message": bot_response,
            "time": bot_time
        })

    return render_template("index.html", chat_history=chat_history)
