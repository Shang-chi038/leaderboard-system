import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Initialize the bot
bot = telebot.TeleBot("YOUR TOKEN HERE")


# Welcome message when the user starts the bot
@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    content = """
    *Welcome to CUPL bot*\n-------------------------------------
You can type /help to learn more about the bot
    """
    bot.send_message(message.chat.id, content, parse_mode="MARKDOWN")


# I implemented this in this manner so as to prevent jampacking the reply
# We can just split this into sections
@bot.message_handler(commands=["help"])
def choose_help(message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("option1", callback_data="option1")
    button2 = InlineKeyboardButton("option2", callback_data="option2")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "What do you need help:", reply_markup=keyboard)





# To send updates to the users when they type anything
custom_responses = {
    "hello": "Hi, how are you doing?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "goodbye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome! 😊"
}

@bot.message_handler(func=lambda message: True)
def send_message(message):
    # Normalize the message text to lowercase
    user_message = message.text.lower()
    
    # Check if the message exists in the predefined responses
    if user_message in custom_responses:
        reply = custom_responses[user_message]
    else:
        reply = "I don't know how to reply to this, please ask ChatGPT"
    
    # Send the response to the user
    bot.reply_to(message, reply)





# Handling Callbacks
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "option1":
        content = """
                *You want to know about...*
                random stuff
                """
        bot.answer_callback_query(call.id, "You chose Option 1")  # To show that option 1 was clicked
        bot.send_message(call.message.chat.id, content, parse_mode="MARKDOWN")
    elif call.data == "option 2":
        content = """
                *You want to know about...*
                random stuff
                """
        bot.answer_callback_query(call.id, "You chose Option 2")  # To show that option 2 was clicked
        bot.send_message(call.message.chat.id, content, parse_mode="MARKDOWN")


# Start the bot
print("CUPL bot is running")
bot.polling()
