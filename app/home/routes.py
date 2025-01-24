from . import home_blueprint
from flask import render_template
from flask import request
from app import bot
import logging

logging.basicConfig(level=logging.DEBUG)


@home_blueprint.route("/", methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        content = request.form["content"]
        bot.send_message(5588640228, content, parse_mode="MARKDOWN")
    return render_template("home/index.html")


@home_blueprint.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)
    return "ok"