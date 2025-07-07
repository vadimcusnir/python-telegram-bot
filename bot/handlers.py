from telegram.ext import CommandHandler, MessageHandler, ContextTypes, filters
from menu import keyboard


async def start(update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ /start activat de:", update.effective_user.username)
    await update.message.reply_text(
        "Salut, sunt botul oficial Vadim Cușnir.\nAlege o opțiune:",
        reply_markup=keyboard,
    )


async def despre(update, context):
    await update.message.reply_text(
        "Sunt Vadim Cușnir – arhitect cognitiv, AI strategist și creator de sisteme educaționale."
    )


async def servicii(update, context):
    await update.message.reply_text(
        "Servicii: Mentorate, cursuri, AI strategy. Vezi https://stan.store/vadimcusnir"
    )


async def contact(update, context):
    await update.message.reply_text("Contact: vadim.kusnir@gmail.com sau @vadimcusnir")


async def gpts(update, context):
    await update.message.reply_text(
        "📚 GPT-uri publice Vadim Cușnir:\n\n"
        "• [Vadim Cușnir Biografie](https://chatgpt.com/g/g-a05oNmcq0-vadim-cusnir-biografie)\n"
        "• [ROAST Standupovka](https://chatgpt.com/g/g-u9mRAHRJk-roast-standupovka)\n"
        "• [Femeia Scrisă](https://chatgpt.com/g/g-67d240aed880819189aad6a08c0f203a-asistent-femeia-scrisa)\n"
        "• [Violența în Familie](https://chatgpt.com/g/g-67e6adee78b081919dbdbfdf1137dc58-consultant-ai-violenta-in-familie)\n"
        "• [Codul Media Moldova](https://chatgpt.com/g/g-67dcf231c018819189d16359637131e1-codul-media-audiovizuale-in-moldova)\n"
        "• [Planul European 2030](https://chatgpt.com/g/g-67ddf0a103e0819188cc4ecc65065920-consultant-in-planul-european-de-dezvoltare)\n"
        "• [Tiny Humans Prompt Generator](https://chatgpt.com/g/g-67d68728ab4c8191a71f9ae27c790da7-tiny-humans-prompt-generator)\n"
        "• [Sarcasm Moldovenesc](https://chatgpt.com/g/g-67953381cd2c8191bd6c7924aa82cbbc-sarcasm-moldovenesc)\n"
        "• [Meaning Architect](https://chatgpt.com/g/g-67556a497658819199b421c242ece94d-meaning-architect)\n"
        "• [Narrio – Scrie o Carte](https://chatgpt.com/g/g-67556fc755848191a69aa350fbef4f78-narrio-speak-write-publish)\n"
        "• [Story Gram – Insta Funnel](https://chatgpt.com/g/g-675573f5e6d881919f82fd433f99e100-story-gram-engage-inspire-convert)\n",
        parse_mode="Markdown",
    )


def register_basic_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("despre", despre))
    app.add_handler(CommandHandler("servicii", servicii))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.Regex("🔍 Despre Vadim"), despre))
    app.add_handler(MessageHandler(filters.Regex("🎓 Servicii"), servicii))
    app.add_handler(MessageHandler(filters.Regex("📩 Contact"), contact))
    app.add_handler(MessageHandler(filters.Regex("🤖 Asistenți GPT"), gpts))
