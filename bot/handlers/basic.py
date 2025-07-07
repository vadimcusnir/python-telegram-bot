# bot/handlers/basic.py
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler

keyboard = ReplyKeyboardMarkup(
    [["🔍 Despre Vadim", "🎓 Servicii"],
     ["🤖 GPT Tool", "📩 Contact"]],
    resize_keyboard=True,
)

# ───────────── callbacks ─────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salut, sunt botul oficial Vadim Cușnir.\nAlege o opțiune:",
        reply_markup=keyboard,
    )

async def despre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sunt Vadim Cușnir – arhitect cognitiv, AI strategist și creator de sisteme educaționale."
    )

async def servicii(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Servicii: Mentorate, cursuri, AI strategy. Vezi https://stan.store/vadimcusnir"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Contact: vadim.kusnir@gmail.com sau @vadimcusnir"
    )

# ───────────── registry ─────────────
def register_basic_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("despre", despre))
    app.add_handler(CommandHandler("servicii", servicii))
    app.add_handler(CommandHandler("contact", contact))
