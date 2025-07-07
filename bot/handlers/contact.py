from telegram import Update
from telegram.ext import ContextTypes

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Contacte directe:\n\n"
        "Telegram: @vadimcusnir\n"
        "E-mail: vadim.kusnir@gmail.com\n"
    )
    await update.message.reply_text(text)
