import os
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "lesson_registry.json")


async def capture_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    now = datetime.now().isoformat()

    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            registry = json.load(f)
    else:
        registry = {}

    registry[str(user_id)] = {"start_time": now, "day": 1}

    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

    await context.bot.send_message(
        chat_id=user_id, text="✅ Te-am înregistrat în Challenge!"
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, capture_user))
    print("Trimite orice mesaj botului din Telegram ca să te înregistrezi...")
    app.run_polling()
