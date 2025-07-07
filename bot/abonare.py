import re
import requests
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

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
    webhook_url = context.bot_data.get("MAKE_WEBHOOK_URL")

    print("📩 Email primit:", email)
    print("➡️ Trimit către webhook:", webhook_url)

    if not is_valid_email(email):
        await update.message.reply_text("❌ Email invalid. Încearcă din nou.")
        return EMAIL

    try:
        response = requests.post(webhook_url, json={"email": email})
        print("📤 Webhook status:", response.status_code)
        if response.status_code == 200:
            await update.message.reply_text("✅ Email primit! Vezi inboxul.")
        else:
            await update.message.reply_text("⚠️ Eroare la trimitere.")
    except Exception as e:
        print("❌ Eroare webhook:", e)
        await update.message.reply_text("⚠️ Eroare de conexiune.")

    return ConversationHandler.END


def register_abonare_handler(app, make_webhook_url):
    app.bot_data["MAKE_WEBHOOK_URL"] = make_webhook_url
    abonare_handler = ConversationHandler(
        entry_points=[CommandHandler("abonare", abonare)],
        states={
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, procesare_email)]
        },
        fallbacks=[],
    )
    app.add_handler(abonare_handler)
