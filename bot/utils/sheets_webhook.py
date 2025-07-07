import requests
import logging

def send_to_sheets(user_id, username, level, full_name, lang, timestamp, answers):
    url = "https://hook.eu2.make.com/zklh9in8rtnt3z8dzi2xhr3f2z9u371f"  # înlocuiește cu webhook-ul real
    data = {
        "user_id": user_id,
        "username": username,
        "level": level,
        "full_name": full_name,
        "language": lang,
        "timestamp": timestamp,
        "answers": answers
    }
    try:
        response = requests.post(url, json=data)
        logging.info(f"📤 Trimitem în Make: {data}")
        logging.info(f"📥 Răspuns Make: {response.status_code} {response.text}")
    except Exception as e:
        logging.error(f"❌ Eroare la trimitere în Make: {e}")
