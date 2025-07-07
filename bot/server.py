# bot/server.py
import os, asyncio
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

# ───── PTB app ───────────────────────────────────────────
application = ApplicationBuilder().token(TOKEN).build()
from bot.handlers.basic import register_basic_handlers
register_basic_handlers(application)

# ───── FastAPI app ───────────────────────────────────────
app = FastAPI()

# ↻ inițializează PTB la pornirea serverului
@app.on_event("startup")
async def _startup():
    await application.initialize()
    await application.start()

# ↻ oprește‑l curat la shutdown (evită crash după câteva secunde)
@app.on_event("shutdown")
async def _shutdown():
    await application.stop()
    await application.shutdown()

# health‑check pentru Railway (GET /)
@app.get("/")
async def root():
    return {"status": "alive"}

# endpoint real pentru Telegram
@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot)
    # nu lăsa excepțiile să termine requestul
    try:
        await application.process_update(update)
    except Exception as e:
        print("[WEBHOOK‑ERROR]", e)
    return {"ok": True}
