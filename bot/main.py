# bot/main.py
import os, asyncio, logging
from pathlib import Path
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
logging.basicConfig(level=logging.INFO)

from bot.handlers.basic import register_basic_handlers
from bot.handlers.subscribe import register_abonare_handler
# adaugă alte register_* aici

async def main():
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    register_basic_handlers(app)
    register_abonare_handler(app)
    # ...

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    logging.info("Bot rulează ↻ polling")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
