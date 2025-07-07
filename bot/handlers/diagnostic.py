from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler, ContextTypes
from bot.utils.sheets_webhook import send_to_sheets
from bot.utils.menu import get_main_menu
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Q1, Q2, Q3, Q4, Q5, Q6, Q7 = range(7)

score_map = {
    'A': 'RUPT',
    'B': 'ALES',
    'C': 'OPERATOR',
    'D': 'TRANSCENDENT'
}

user_answers = {}

questions = [
    ("Ce simți când postezi online despre ceea ce faci?", ["A. Frică de ridicol", "B. Oboseală", "C. Entuziasm superficial", "D. Tensiune controlată"]),
    ("Ce crezi despre bani?", ["A. Trebuie munciți din greu", "B. Recompensa pentru expertiză", "C. Vin dacă știi să vinzi", "D. Sunt ecoul vocii tale"]),
    ("Cum reacționezi la AI?", ["A. Curios, dar nu-l înțeleg", "B. Îl folosesc pentru texte", "C. L-am antrenat deja", "D. Nu îl folosesc"]),
    ("Care e cea mai mare frică a ta în carieră?", ["A. Să nu fiu văzut", "B. Să nu fiu înțeles", "C. Să nu fiu replicabil", "D. Să fiu diluat"]),
    ("Ce înseamnă ‘voce’ pentru tine?", ["A. Modul de exprimare", "B. Tonul & stilul", "C. Filtru care exclude", "D. Algoritmul interior"]),
    ("Când ești cel mai productiv?", ["A. Când sunt motivat", "B. Când am presiune", "C. Când am claritate", "D. Când decide sistemul"]),
    ("Ce vrei cu adevărat să devii?", ["A. Liber", "B. Cunoscut", "C. Monetizabil", "D. Nemuritor"])
]

async def start_diagnostic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_answers[update.effective_chat.id] = []
    await update.message.reply_text(
        "🧠 Acest test inițiatic conține 7 întrebări simbolice.\n\n"
        "Alege opțiunea care te reprezintă cel mai mult.\n"
        "La final vei primi un *badge personalizat* și un *link unic* de activare.\n\n"
        "👇 Să începem:"
    )
    q_text, options = questions[0]
    reply_markup = ReplyKeyboardMarkup.from_column(options, resize_keyboard=True)
    await update.message.reply_text(q_text, reply_markup=reply_markup)
    return Q1

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE, step: int) -> int:
    user_id = update.effective_chat.id
    text = update.message.text.strip()
    logger.info(f"[STEP {step}] INPUT: {text}")
    if not text or text[0].upper() not in ['A', 'B', 'C', 'D']:
        await update.message.reply_text("⚠️ Alege o opțiune validă.")
        return step
    answer = text[0].upper()
    user_answers[user_id].append(answer)
    if step + 1 < len(questions):
        q_text, options = questions[step + 1]
        reply_markup = ReplyKeyboardMarkup.from_column(options, resize_keyboard=True)
        await update.message.reply_text(q_text, reply_markup=reply_markup)
        return step + 1
    else:
        return await final_result(update, context)

async def final_result(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_chat.id
    answers = user_answers.get(user_id, [])
    dominant = max(set(answers), key=answers.count)
    level = score_map.get(dominant, "RUPT")
    await update.message.reply_text("📊 Testul s-a încheiat. Iată rezultatul tău:", reply_markup=ReplyKeyboardRemove())
    send_to_sheets(
        user_id=user_id,
        username=update.effective_user.username,
        level=level,
        full_name=update.effective_user.full_name,
        lang=update.effective_user.language_code,
        timestamp=datetime.now().isoformat(),
        answers=user_answers[user_id]
    )
    messages = {
        'RUPT': ("Ești RUPT. Începe cu Antișcoala™.", "https://notadoi.com/antiscoala"),
        'ALES': ("Ești ALES. Intră în Lounge™.", "https://notadoi.com/lounge"),
        'OPERATOR': ("Ești OPERATOR. Automatizează cu mAInd.", "https://notadoi.com/maind"),
        'TRANSCENDENT': ("Ești TRANSCENDENT. Activează-ți mitul.", "https://notadoi.com/inteligentia")
    }
    message_text, url = messages[level]
    reply_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton("🔗 Deschide", url=url))
    await update.message.reply_text(message_text, reply_markup=reply_markup)
    await update.message.reply_text("🔁 Revii la /start pentru alte opțiuni.", reply_markup=get_main_menu())
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Diagnosticul a fost oprit.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

async def q1(update, context): return await handle_question(update, context, Q1)
async def q2(update, context): return await handle_question(update, context, Q2)
async def q3(update, context): return await handle_question(update, context, Q3)
async def q4(update, context): return await handle_question(update, context, Q4)
async def q5(update, context): return await handle_question(update, context, Q5)
async def q6(update, context): return await handle_question(update, context, Q6)
async def q7(update, context): return await handle_question(update, context, Q7)
