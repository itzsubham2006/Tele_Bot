import telebot
from telebot import types
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))



career_data = {
    "ml": {
        "name": "Machine Learning",
        "roadmap": "https://roadmap.sh/ai-engineer",
        "resources": [
            "Book: Hands-On ML by Aurelien Geron",
            "Course: Andrew Ng ML (Coursera)",
            "PDF: ML Cheatsheet",
            "Link: scikit-learn docs - scikit-learn.org",
            "Link: TensorFlow tutorials - tensorflow.org"
        ]
    },
    "web": {
        "name": "Web Development",
        "roadmap": "https://roadmap.sh/full-stack",
        "resources": [
            "Book: Eloquent JavaScript",
            "Course: The Odin Project (theodinproject.com)",
            "PDF: Web Dev Checklist",
            "Link: MDN Web Docs - developer.mozilla.org",
            "Link: freeCodeCamp - freecodecamp.org"
        ]
    }
}

notes_data = {
    "3rd": {
        "name": "3rd Semester",
        "subjects": {
            "maths": "Mathematics",
            "dsa": "Data Structures & Algorithms",
            "java": "Java Programming"
        }
    },
    "4th": {
        "name": "4th Semester",
        "subjects": {
            "maths": "Mathematics",
            "dsa": "Data Structures & Algorithms",
            "java": "Java Programming"
        }
    }
}

subject_pdfs = {
    "3rd_maths": [
        "http://example.com/3rd_maths_notes.pdf",
        "http://example.com/3rd_maths_practice.pdf"
    ],
    "3rd_dsa": [
        "http://example.com/3rd_dsa_notes.pdf",
        "http://example.com/3rd_dsa_lab.pdf"
    ],
    "3rd_java": [
        "http://example.com/3rd_java_notes.pdf",
        "http://example.com/3rd_java_practical.pdf"
    ],
    "4th_maths": [
        "http://example.com/4th_maths_notes.pdf",
        "http://example.com/4th_maths_practice.pdf"
    ],
    "4th_dsa": [
        "http://example.com/4th_dsa_notes.pdf",
        "http://example.com/4th_dsa_lab.pdf"
    ],
    "4th_java": [
        "http://example.com/4th_java_notes.pdf",
        "http://example.com/4th_java_assignments.pdf"
    ]
}



def main_menu_kb():
    mk = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for b in ["Career", "Notes", "GitHub", "Time", "About", "Help"]:
        mk.add(types.KeyboardButton(b))
    return mk



@bot.message_handler(commands=['start'])
def cmd_start(msg):
    bot.send_message(
        msg.chat.id,
        "Hey, press /start to see everything I can do.\n\n"
        "This bot helps you with:\n"
        "- Career roadmaps + resources\n"
        "- Semester notes (PDFs)\n"
        "- GitHub, time, and more\n\n"
        "Just hit /start and the menu will show up.",
        reply_markup=main_menu_kb()
    )
    bot.set_my_commands([
        types.BotCommand("start", "Start the bot"),
        types.BotCommand("notes", "Semester-wise notes"),
        types.BotCommand("career", "Career resources"),
        types.BotCommand("help", "All commands"),
    ])



@bot.message_handler(commands=['help'])
def cmd_help(msg):
    bot.reply_to(msg,
        "/start  - Start + show menu\n"
        "/notes  - Browse notes by semester\n"
        "/career - Career roadmaps & resources\n"
        "/help   - This message\n\n"
        "Keyboard buttons:\n"
        "Career, Notes, GitHub, Time, About, Help"
    )



@bot.message_handler(commands=['notes'])
def cmd_notes(msg):
    show_notes_menu(msg)



@bot.message_handler(commands=['career'])
def cmd_career(msg):
    show_career_menu(msg)



def show_career_menu(msg_or_id):
    chat_id = msg_or_id.chat.id if hasattr(msg_or_id, 'chat') else msg_or_id
    mk = types.InlineKeyboardMarkup(row_width=2)
    mk.add(
        types.InlineKeyboardButton("Machine Learning", callback_data="c_ml"),
        types.InlineKeyboardButton("Web Development", callback_data="c_web"),
        types.InlineKeyboardButton("<< Back", callback_data="c_back")
    )
    bot.send_message(chat_id, "== Career / Goals ==\n\nPick a field:", reply_markup=mk)

def show_career_detail(call, key):
    c = career_data[key]
    lines = [f"== {c['name']} ==\n"]
    lines.append("> Roadmap:")
    lines.append(f"  {c['roadmap']}")
    lines.append("")
    lines.append("> Resources:")
    for r in c["resources"]:
        lines.append(f"  - {r}")
    lines.append("")
    

    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("<< Back", callback_data="c_back"))
    bot.edit_message_text("\n".join(lines), call.message.chat.id, call.message.message_id, reply_markup=mk, disable_web_page_preview=True)



def show_notes_menu(msg_or_id):
    chat_id = msg_or_id.chat.id if hasattr(msg_or_id, 'chat') else msg_or_id
    mk = types.InlineKeyboardMarkup(row_width=2)
    mk.add(
        types.InlineKeyboardButton("3rd Semester", callback_data="n_3rd"),
        types.InlineKeyboardButton("4th Semester", callback_data="n_4th"),
        types.InlineKeyboardButton("<< Back", callback_data="n_back")
    )
    bot.send_message(chat_id, "== Notes Library ==\n\nPick your semester:", reply_markup=mk)

def show_subjects(call, sem):
    info = notes_data[sem]
    mk = types.InlineKeyboardMarkup(row_width=1)
    for sk, sn in info["subjects"].items():
        mk.add(types.InlineKeyboardButton(sn, callback_data=f"s_{sem}_{sk}"))
    mk.add(types.InlineKeyboardButton("<< Back to semesters", callback_data="n_back"))
    bot.edit_message_text(
        f"== {info['name']} ==\n\nPick a subject:",
        call.message.chat.id, call.message.message_id,
        reply_markup=mk
    )

def show_pdfs(call, sem, sub):
    info = notes_data[sem]
    sub_name = info["subjects"][sub]
    pdf_key = f"{sem}_{sub}"
    pdfs = subject_pdfs.get(pdf_key, ["(no PDFs added yet)"])
    lines = [f"== {sub_name} ({info['name']}) ==\n"]
    lines.append("> PDFs:")
    for p in pdfs:
        lines.append(f"  - {p}")
    lines.append("")
    

    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("<< Back to subjects", callback_data=f"b_{sem}"))
    bot.edit_message_text(
        "\n".join(lines),
        call.message.chat.id, call.message.message_id,
        reply_markup=mk, disable_web_page_preview=True
    )



@bot.callback_query_handler(func=lambda c: True)
def handle_cb(call):
    d = call.data

    
    if d == "c_ml":
        show_career_detail(call, "ml")
    elif d == "c_web":
        show_career_detail(call, "web")
    elif d == "c_back":
        show_career_menu(call.message.chat.id)

    elif d == "n_back":
        show_notes_menu(call.message.chat.id)
    elif d.startswith("n_"):
        sem = d.split("_", 1)[1]
        show_subjects(call, sem)
    elif d.startswith("b_"):
        sem = d.split("_", 1)[1]
        show_subjects(call, sem)
    elif d.startswith("s_"):
        parts = d.split("_")
        if len(parts) == 3:
            show_pdfs(call, parts[1], parts[2])

    bot.answer_callback_query(call.id)


@bot.message_handler(func=lambda m: True)
def handle_text(msg):
    t = msg.text

    if t == "Career":
        show_career_menu(msg)
    elif t == "Notes":
        show_notes_menu(msg)
    elif t == "GitHub":
        bot.reply_to(msg, "My GitHub:\nhttps://github.com/")
    elif t == "Time":
        now = datetime.now()
        bot.reply_to(msg, now.strftime("%A, %d %B %Y\n%I:%M:%S %p"))
    elif t == "About":
        bot.reply_to(msg,
            "Subham Pathak\n"
            "3rd year CSE\n"
            "CIT Kokrajhar\n"
            "AI/ML + Backend"
        )
    elif t == "Help":
        cmd_help(msg)
    else:
        bot.reply_to(msg, "I dont understand. Type /help")



print("Bot running...")
bot.infinity_polling()
