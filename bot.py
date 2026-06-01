import telebot
from telebot import types
from datetime import datetime
import random
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )

    buttons = [
        "AI Chat",
        "Weather",
        "Notes",
        "Todo",
        "GitHub",
        "Joke",
        "Movies",
        "Quote",
        "Date",
        "Time",
        "About Me",
        "Help"
    ]

    for btn in buttons:
        markup.add(types.KeyboardButton(btn))

    welcome_text = """
*Welcome to Telegro AI Assistant*

━━━━━━━━━━━━━━━━━━━

>> Hello!

I'm your personal Telegram assistant.

    Features Available:

    AI Chat
    Weather
    Notes
    Todo List
    GitHub
    Jokes
    Movies
    Quotes
    Date & Time

━━━━━━━━━━━━━━━━━━━

>>  Created by Subham Pathak
>>  Powered by Python

Select any option below.
"""

    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(
        message,
        """
    AVAILABLE COMMANDS

/start      - Start Bot
/help       - Show Commands
/name       - Creator Name
/address    - Address
/about      - About Bot
/date       - Current Date
/time       - Current Time
/joke       - Random Joke
/quote      - Motivation Quote
/college    - College Name
/course     - Course
/skills     - Skills
/contact    - Contact Info
        """
    )


@bot.message_handler(commands=['name'])
def name(message):
    bot.reply_to(message, "Creator: Subham Pathak")


@bot.message_handler(commands=['address'])
def address(message):
    bot.reply_to(
        message,
        "Rowta, Udalguri District, Assam, India"
    )


@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(
        message,
        "Telegro AI Assistant\nCreated using Python and TeleBot."
    )


@bot.message_handler(commands=['college'])
def college(message):
    bot.reply_to(
        message,
        "Central Institute of Technology, Kokrajhar"
    )


@bot.message_handler(commands=['course'])
def course(message):
    bot.reply_to(
        message,
        "Computer Science and Engineering"
    )


@bot.message_handler(commands=['skills'])
def skills(message):
    bot.reply_to(
        message,
        """
Skills

• Python
• Flask
• FastAPI
• HTML
• CSS
• JavaScript
• Machine Learning
• Deep Learning
• Git & GitHub
"""
    )


@bot.message_handler(commands=['contact'])
def contact(message):
    bot.reply_to(
        message,
        "Contact: lastw5232@gmail.com"
    )


@bot.message_handler(commands=['date'])
def date(message):
    bot.reply_to(
        message,
        f"{datetime.now().strftime('%d-%m-%Y')}"
    )


@bot.message_handler(commands=['time'])
def time(message):
    bot.reply_to(
        message,
        f"{datetime.now().strftime('%H:%M:%S')}"
    )



@bot.message_handler(commands=['joke'])
def joke(message):

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Python is my favorite snake.",
        "Debugging is like being a detective in a crime movie where you're also the criminal.",
        "There are 10 kinds of people: those who understand binary and those who don't."
    ]

    bot.reply_to(message, random.choice(jokes))


@bot.message_handler(commands=['quote'])
def quote(message):

    quotes = [
        "Success comes from consistency.",
        "Discipline beats motivation.",
        "Small progress is still progress.",
        "Never stop learning.",
        "Dream big. Start small. Act now."
    ]

    bot.reply_to(message, random.choice(quotes))


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):

    text = message.text

    if text == "AI Chat":
        bot.reply_to(
            message,
            "AI Chat feature coming soon!"
        )

    elif text == "Weather":
        bot.reply_to(
            message,
            "Weather API will be added soon."
        )

    elif text == "Notes":
        bot.reply_to(
            message,
            "Notes feature coming soon."
        )

    elif text == "Todo":
        bot.reply_to(
            message,
            "Todo Manager coming soon."
        )

    elif text == "GitHub":
        bot.reply_to(
            message,
            "GitHub Profile: https://github.com/"
        )

    elif text == "Joke":
        joke(message)

    elif text == "Movies":
        bot.reply_to(
            message,
            "Movie recommendations coming soon."
        )

    elif text == "Quote":
        quote(message)

    elif text == "Date":
        date(message)

    elif text == "Time":
        time(message)

    elif text == "About Me":
        bot.reply_to(
            message,
            """
👤 Subham Pathak

    CSE Student
    Central Institute of Technology, Kokrajhar
    Interested in AI/ML
    Backend Development
    Aspiring Game Developer
"""
        )

    elif text == "Help":
        help_command(message)

    else:
        bot.reply_to(
            message,
            "I don't understand that command.\nUse /help"
        )


print("Bot is running...")
bot.infinity_polling()