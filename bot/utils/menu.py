from telegram import ReplyKeyboardMarkup

def get_main_menu():
    buttons = [
        ["🧠 Diagnostic Antișcoala"],
        ["📬 Contact", "🧰 Asistenți GPTs"],
        ["🔒 Acces Lounge"]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
