import os, asyncio, logging
from pathlib import Path
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
logging.basicConfig(level=logging.INFO)

from bot.handlers.basic import register_basic_handlers

async def main():
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    register_basic_handlers(app)

    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        webhook_url=os.getenv("WEBHOOK_URL")
    )

if __name__ == "__main__":
    asyncio.run(main())
