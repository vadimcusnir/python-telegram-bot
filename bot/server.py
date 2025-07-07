# bot/server.py
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
app = FastAPI()

application = ApplicationBuilder().token(BOT_TOKEN).build()

from bot.handlers.basic import register_basic_handlers
register_basic_handlers(application)

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return {"status": "ok"}
