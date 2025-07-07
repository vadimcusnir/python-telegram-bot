import os
import json
import sys
from telegram import Bot
from dotenv import load_dotenv
from datetime import datetime
import asyncio

# 🔐 Încarcă token
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

# 📁 Căi fișiere
BASE_DIR = os.path.dirname(__file__)
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")
REGISTRY_PATH = os.path.join(BASE_DIR, "lesson_registry.json")


# ⏱️ Delay fix între mesaje
def get_delay(filename):
    return 10  # secunde


# 📤 Trimite lecția curentă pentru fiecare user
async def send_daily_lessons():
    if not os.path.exists(REGISTRY_PATH):
        print("No registry found.")
        return

    with open(REGISTRY_PATH, "r") as f:
        registry = json.load(f)

    for user_id, data in registry.items():
        current_day = data.get("day", 1)
        lesson_folder = f"{current_day:02d}_"
        lesson_path = None

        for name in os.listdir(LESSONS_DIR):
            if name.startswith(lesson_folder):
                lesson_path = os.path.join(LESSONS_DIR, name)
                break

        if not lesson_path or not os.path.isdir(lesson_path):
            print(f"❌ No lesson folder found for day {current_day}")
            continue

        print(f"\n✅ Trimit lecția {current_day} către user {user_id}")
        files = sorted(os.listdir(lesson_path))

        for filename in files:
            full_path = os.path.join(lesson_path, filename)
            print(f"📄 Fișier: {filename}")

            if filename.endswith(".txt"):
                with open(full_path, "r") as f:
                    print("✉️ Trimit text...")
                    await bot.send_message(chat_id=user_id, text=f.read())

            elif filename.endswith(".pdf") or filename.endswith(".docx"):
                with open(full_path, "rb") as f:
                    print("📎 Trimit document...")
                    await bot.send_document(chat_id=user_id, document=f)

            elif filename.endswith(".jpg") or filename.endswith(".png"):
                with open(full_path, "rb") as f:
                    print("🖼️ Trimit imagine...")
                    await bot.send_photo(chat_id=user_id, photo=f)

            elif filename.endswith(".mp4"):
                with open(full_path, "rb") as f:
                    print("🎥 Trimit video...")
                    await bot.send_video(chat_id=user_id, video=f)

            elif filename.endswith(".json") and "feedback" in filename:
                with open(full_path, "r") as f:
                    data = json.load(f)
                    question = data.get("q")
                    options = data.get("options")
                    if question and options:
                        print("📊 Trimit sondaj...")
                        await bot.send_poll(
                            chat_id=user_id,
                            question=question,
                            options=options,
                            is_anonymous=False,
                        )

            await asyncio.sleep(get_delay(filename))

        registry[str(user_id)]["day"] += 1

    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)


# ♻️ Reset ziua la 1 pentru toți userii
def reset_day_to_one():
    if not os.path.exists(REGISTRY_PATH):
        print("⚠️ Nu există lesson_registry.json")
        return

    with open(REGISTRY_PATH, "r") as f:
        registry = json.load(f)

    for user_id in registry:
        registry[user_id]["day"] = 1
        registry[user_id]["start_time"] = datetime.now().isoformat()

    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

    print("🔁 Toți userii au fost resetați la ziua 1")


# ▶️ Rulează principal
if __name__ == "__main__":
    if "--reset" in sys.argv:
        reset_day_to_one()
    else:
        asyncio.run(send_daily_lessons())
