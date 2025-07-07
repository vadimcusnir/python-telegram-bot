from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Scrie Recenzie pe Google", url="https://g.page/r/CZW6D1JMku7KEAE/review")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "1100+ Oameni au Scris Recenzii publice despre Vadim Cușnir. Vrei să îl susții și tu? Îți ia 15 secunde:",
        reply_markup=reply_markup
    )
