import os

from dotenv import load_dotenv
from flask import Flask
from telebot import TeleBot

from config import config_dict

load_dotenv()

bot = TeleBot(os.getenv("BOT_API_KEY"))

def create_app(config="default"):
    app = Flask(__name__)
    app.config.from_object(config_dict[config])
    config_dict[config].init_app(app)

    from .home import home_blueprint
    app.register_blueprint(home_blueprint, url_prefix = "/")

    bot.remove_webhook()
    bot.set_webhook(url=os.getenv("WEBHOOK_URL"))

    
    return app
