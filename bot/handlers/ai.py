import openai
import os
from telegram.ext import CallbackContext
from telegram import Update
from telegram.ext import ContextTypes

# Ia cheia API din .env
openai.api_key = os.getenv("OPENAI_API_KEY")
AI_ACTIVE_USERS = set()

def activate_ai(update, context):
    user_id = update.effective_user.id
    AI_ACTIVE_USERS.add(user_id)
    update.message.reply_text(
        "💡 Modul ChatGPT este ACTIVAT! Scrie orice mesaj și vei primi răspuns AI.\n\nTrimite /stopgpt pentru a reveni la meniu."
    )

def deactivate_ai(update, context):
    user_id = update.effective_user.id
    AI_ACTIVE_USERS.discard(user_id)
    update.message.reply_text(
        "🤖 Modul ChatGPT a fost DEZACTIVAT. Revii la meniul normal."
    )

async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"🧾 Mesaj primit: '{update.message.text}'")
    await update.message.reply_text("Am primit mesajul tău.")

