# main_webhook.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("bot.server:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
