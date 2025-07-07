from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.menu import get_main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = get_main_menu()
    await update.message.reply_text(
        "👋 Bun venit în Antișcoala Vadim Cușnir™.\n\n"
        "Aici nu e despre educație. E despre selecție.\n\n"
        "Alege de mai jos cum vrei să începi:",
        reply_markup=reply_markup
    )

async def help_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ Comenzi disponibile:\n"
        "/start – Meniu principal\n"
        "/diagnostic – Test inițiatic Antișcoala\n"
        "/public_gpts – Acces GPT-uri deschise\n"
        "/contact – Scrie-ne direct"
    )
