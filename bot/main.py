import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers.basic import register_basic_handlers
from handlers.subscribe import register_abonare_handler

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = ApplicationBuilder().token(TOKEN).build()
print("👂 Listening on:", WEBHOOK_URL)

register_basic_handlers(app)
register_abonare_handler(app, WEBHOOK_URL)


async def run_webhook():
    print("🚀 Pornit în mod WEBHOOK")
    await app.initialize()
    await app.start()
    await app.updater.start_webhook(
        listen="0.0.0.0",
        port=8000,
        url_path="/webhook",
        webhook_url=WEBHOOK_URL,
    )
    print("🌐 Webhook activ. Railway blocat.")
    import asyncio

    await asyncio.Event().wait()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run_webhook())
