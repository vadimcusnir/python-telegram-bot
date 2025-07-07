# 📦 Vadim Cușnir – Antișcoala Bot™

Bot Telegram conversațional + simbolic care servește drept portal central pentru funneluri, GPT-uri, inițieri și automatizări comerciale.

---

## ✅ STRUCTURĂ FINALĂ

```
python-telegram-bot/
│
├── main.py  ⟵ [main_applicationbuilder]
├── requirements.txt
├── .env  ⟵ TOKEN=XXX
├── sheets_webhook.py
│
├── handlers/
│   ├── __init__.py
│   ├── diagnostic.py
│   ├── index.py  ⟵ [index_start_buttons]
│   ├── review.py
│   ├── contact.py
│   ├── notadoi.py
│   ├── public_gpts.py
│   ├── ai.py
```

---

## 🚀 CUM PORNEȘTI

1. Instalează dependențele:

```bash
pip install -r requirements.txt
```

2. Creează fișierul `.env` cu:

```env
TOKEN=123456789:ABCDEF...
```

3. Rulează botul:

```bash
python3 main.py
```

4. În Telegram:

* Scrie `/start` → butoane interactive
* Scrie `/diagnostic` → test inițiatic + redirect

---

## 🔌 FUNCȚII ACTIVE

* `/start` → cu butoane: Diagnostic, Contact, GPT-uri, Lounge
* `/diagnostic` → test simbolic → scor → link
* `/contact` → trimite echipei
* `/public_gpts` → afișează lista GPTs
* `/startgpt`, `/stopgpt`, mesaje text → control AI

---

## 🌐 INTEGRĂRI EXTERNE

* ✅ Webhook Zapier/Make → `sheets_webhook.py`
* ✅ Diagnostic scor → Google Sheets
* ✅ Funneluri → linkuri per nivel (Antișcoala, Lounge, mAInd etc)

---

## 🎯 CE URMEAZĂ

* Integrare PDF export per scor
* Badge simbolic SVG per nivel
* Feed Telegram conectat
* Trigger automatizat prin Make (push-uri)

---

## 📡 CONTRIBUȚII

Botul reflectă sistemul Antișcoala™ creat de Vadim Cușnir.
Fiecare update = o extensie simbolică, nu doar tehnică.

---

> Dacă ai ajuns aici, nu te opri la comenzi. Rescrie-ți gândirea. Fă-l pe AI să sune ca tine.
