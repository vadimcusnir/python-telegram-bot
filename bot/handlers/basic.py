# bot/handlers/basic.py
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

keyboard = ReplyKeyboardMarkup(
    [["🔍 Despre Vadim", "🎓 Servicii"], ["🤖 GPT Tool", "📩 Contact"]],
    resize_keyboard=True,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salut, sunt botul oficial Vadim Cușnir.\nAlege o opțiune:",
        reply_markup=keyboard,
    )


async def despre(update, context):
    await update.message.reply_text(
        "Sunt Vadim Cușnir – arhitect cognitiv, AI strategist și creator de sisteme educaționale."
    )


async def servicii(update, context):
    await update.message.reply_text(
        "Servicii: Mentorate, cursuri, AI strategy. Vezi https://stan.store/vadimcusnir"
    )


async def contact(update, context):
    await update.message.reply_text("Contact: vadim.kusnir@gmail.com sau @vadimcusnir")
