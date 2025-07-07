import os
import re
import logging
import requests
from threading import Event
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

# 🔐 Încarcă variabilele din .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# 🧠 Logging
logging.basicConfig(level=logging.INFO)

# 🎛 Tastatură principală
keyboard = ReplyKeyboardMarkup(
    [["🔍 Despre Vadim", "🎓 Servicii"], ["🤖 GPT Tool", "📩 Contact"]],
    resize_keyboard=True,
)


# ✅ Comenzi simple
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ /start activat de:", update.effective_user.username)
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


# 📩 Abonare
EMAIL = range(1)


def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email)


async def abonare(update, context):
    print("🟣 /abonare activat de:", update.effective_user.username)
    await update.message.reply_text(
        "📩 Scrie adresa ta de email pentru a primi bonusul."
    )
    return EMAIL


async def procesare_email(update, context):
    email = update.message.text.strip()
    print("📩 Email primit:", email)
    print("➡️ Trimit către webhook:", WEBHOOK_URL)

    if not is_valid_email(email):
        await update.message.reply_text("❌ Email invalid. Încearcă din nou.")
        return EMAIL

    try:
        response = requests.post(WEBHOOK_URL, json={"email": email})
        print("📤 Webhook status:", response.status_code)
        if response.status_code == 200:
            await update.message.reply_text("✅ Email primit! Vezi inboxul.")
        else:
            await update.message.reply_text("⚠️ Eroare la trimitere.")
    except Exception as e:
        print("❌ Eroare webhook:", e)
        await update.message.reply_text("⚠️ Eroare de conexiune.")

    return ConversationHandler.END


# 🔧 Inițializare aplicație
app = ApplicationBuilder().token(TOKEN).build()

# ➕ Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("despre", despre))
app.add_handler(CommandHandler("servicii", servicii))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(MessageHandler(filters.Regex("🔍 Despre Vadim"), despre))
app.add_handler(MessageHandler(filters.Regex("🎓 Servicii"), servicii))
app.add_handler(MessageHandler(filters.Regex("📩 Contact"), contact))

abonare_handler = ConversationHandler(
    entry_points=[CommandHandler("abonare", abonare)],
    states={EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, procesare_email)]},
    fallbacks=[],
)
app.add_handler(abonare_handler)

# 🚀 Pornire Webhook + Blocare Railway
if __name__ == "__main__":
    print("🚀 Pornit în mod WEBHOOK")

    app.run_webhook(listen="0.0.0.0", port=8000, webhook_url=WEBHOOK_URL)

    print("🌐 Webhook activ. Blocare infinită Railway via threading.Event().wait()")
    Event().wait()
