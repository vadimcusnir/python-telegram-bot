from telegram import Update
from telegram.ext import ContextTypes

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Ai selectat: {text}")
