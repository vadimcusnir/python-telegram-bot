# quick_test.py
import os, asyncio, logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

load_dotenv()
logging.basicConfig(level=logging.INFO)

async def hello(update, context):
    await update.message.reply_text("✅ Bot OK – test reușit")

async def main():
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("test", hello))
    print("→ Trimite /test botului în Telegram")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()   # ține procesul deschis

if __name__ == "__main__":
    asyncio.run(main())
