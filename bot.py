import telebot
from telebot import types
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

BASE = r"C:\Users\Subham Pathak\Desktop\AI\PROJECTS\Tele_bot"

career_data = {
    "ml": {
        "name": "Machine Learning",
        "roadmap": "Python -> FastAPI/Backend -> SQL --> Postgrsql --> Machine Learning (Mathematics + concept)  ---> Deep Learning --> GenAI ---> Agentic AI --> MLOps --> (DSA + 𝗣𝗥𝗢𝗝𝗘𝗖𝗧𝗦)",
        "resources": [
            "Python : https://www.youtube.com/live/1z5-O7-5AXk?si=Z_cQAlWASovCFitL",
            "FastAPI : FastAPI by CampusX (search in yt)",
            "SQL : MYSQL by CampusX (youtube)",
            "Postgresql : Any playlist (youtube)",
            "Machine Learning : Machine Learning by CampusX (youtube)",
            "Deep Learning : Deep Learning by CampusX (yt)",
            "GenAI : GenAI by CampusX (yt)",
            "Book: Hands-On ML by Aurelien Geron",
            "Course: Andrew Ng ML (Coursera)",
            "PDF: ML Cheatsheet",
            "Link: scikit-learn docs - scikit-learn.org",
            "Link: TensorFlow tutorials - tensorflow.org"
        ]
    },
    "web": {
        "name": "Web Development",
        "roadmap": "",
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
            "python": "Python Programming",
            "electronics": "Digital Electronics",
            "iks": "Indian Knowledge System"
        }
    },
    "4th": {
        "name": "4th Semester",
        "subjects": {
            "maths": "Mathematics",
            "daa": "Design & Analysis of Algorithms",
            "java": "Java Programming",
            "coa": "Computer Organization & Architecture"
        }
    }
}

subject_files = {
    "3rd_maths": [
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L1-Probability.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L2-Discrete Random Variables.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L3-Continuous Random Variables.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L3-Continuous Random Variables-part.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L4-Expectation - Variance.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L5- Moments.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-L6-Joint Distribution Functions.pdf"),
        os.path.join(BASE, r"Notes\3rd_sem\Maths\AAB\UMA301-2025-Pre-Requisites-Permutation-Combination.docx.pdf"),
    ],
    "3rd_dsa": [
        os.path.join(BASE, r"Notes\3rd_sem\DSA\DKR_final_final.pdf"),
    ],
    "3rd_electronics": [
        os.path.join(BASE, r"Notes\3rd_sem\Digital Electronics\AGM_final.pdf"),
    ],
    "4th_maths": [
        os.path.join(BASE, r"Notes\4th_sem\MATHS\function 2.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\MATHS\function.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\MATHS\GCR-II_FINAL.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\MATHS\GCR.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\MATHS\Graph Theory Notes_GCR.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\MATHS\Relation-1.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\MATHS\SMD (1).pdf"),
    ],
    "4th_java": [
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Access Modifiers in Java Examples.docx.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Array.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Exception Handling.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\inheritence.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Java String.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Multithreading in Java.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Packages.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\static keyword in Java.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\this_keyword.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\UCS403 Tutorial 1.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\JAVA\Constructors in Java.docx"),
    ],
    "4th_daa": [
        os.path.join(BASE, r"Notes\4th_sem\Design&Analysis\final.pdf"),
    ],
    "4th_coa": [
        os.path.join(BASE, r"Notes\4th_sem\COA\COA.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\COA\COA_BOOKS\Computer System Architecture 3rd Edition-M Morris Mano.pdf"),
        os.path.join(BASE, r"Notes\4th_sem\COA\COA_BOOKS\William Stallings - Computer Organization and Architecture Designing for Performance (8th Edition).pdf"),
    ],
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

def send_pdfs(call, sem, sub):
    info = notes_data[sem]
    sub_name = info["subjects"][sub]
    pdf_key = f"{sem}_{sub}"
    files = subject_files.get(pdf_key)

    if not files:
        bot.edit_message_text(
            f"No PDFs added for {sub_name} yet.",
            call.message.chat.id, call.message.message_id
        )
        return

  
    names = "\n".join(f"  - {os.path.basename(f)}" for f in files)
    bot.edit_message_text(
        f"Sending {len(files)} file(s) for {sub_name}:\n\n{names}",
        call.message.chat.id, call.message.message_id
    )

    for f in files:
        if os.path.exists(f):
            with open(f, "rb") as fh:
                bot.send_document(call.message.chat.id, fh, caption=os.path.basename(f))
        else:
            bot.send_message(call.message.chat.id, f"File not found: {os.path.basename(f)}")

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
            send_pdfs(call, parts[1], parts[2])

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

print("Bot is running heheheheheeee...")
bot.infinity_polling()
