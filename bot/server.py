import os, asyncio
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

application = ApplicationBuilder().token(TOKEN).build()
from bot.handlers.basic import register_basic_handlers
register_basic_handlers(application)

app = FastAPI()

@app.on_event("startup")
async def on_start():
    await application.initialize()
    await application.start()

async def _keep_alive():
    while True:
        await asyncio.sleep(60)

@app.on_event("shutdown")
async def on_stop():
    await app_tg.stop()
    await app_tg.shutdown()

@app.get("/")
async def health():
    return {"status": "alive"}

@app.post("/webhook")
async def telegram_webhook(req: Request):
    try:
        data = await req.json()
        update = Update.de_json(data, application.bot)
        asyncio.create_task(application.process_update(update))
        print("[WEBHOOK] Update accepted.")
    except Exception as e:
        print("[WEBHOOK‑ERROR]", e)
    return {"ok": True}

