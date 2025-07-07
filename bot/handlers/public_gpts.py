from telegram import Update
from telegram.ext import ContextTypes

async def public_gpts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🧠 *ASISTENȚI GPTs*\n"
        "_Toate sunt create de Vadim Cușnir și sunt publice. Le găsești aici:_ [chatgpt.com/gpts](https://chatgpt.com/gpts)\n\n"

        "*🔹 Identitate & Personalitate*\n"
        "*Vadim Cușnir – Biografie*\n"
        "_Asistentul oficial. Cunoaște biografia completă, detalii personale, trăsături de personalitate._\n"
        "[Deschide](https://chatgpt.com/g/g-a05oNmcq0-vadim-cusnir-biografie)\n\n"

        "*🔹 Umor, Sarcasm & ROAST*\n"
        "*ROAST Standupovka*\n"
        "_Glume ROAST despre comedianții Standupovka._\n"
        "[Deschide](https://chatgpt.com/g/g-u9mRAHRJk-roast-standupovka)\n"
        "*Sarcasm Moldovenesc*\n"
        "_Glume tăioase despre stilul moldovenesc._\n"
        "[Deschide](https://chatgpt.com/g/g-67953381cd2c8191bd6c7924aa82cbbc-sarcasm-moldovenesc)\n"
        "*Femeia Scrisă*\n"
        "_Felicitări puternice și ingenioase pentru femei._\n"
        "[Deschide](https://chatgpt.com/g/g-67d240aed880819189aad6a08c0f203a-asistent-femeia-scrisa)\n\n"

        "*🔹 Consultanță Tematică & Legală*\n"
        "*Violența în Familie*\n"
        "[Deschide](https://chatgpt.com/g/g-67e6adee78b081919dbdbfdf1137dc58-consultant-ai-violenta-in-familie)\n"
        "*Codul Media – Moldova*\n"
        "[Deschide](https://chatgpt.com/g/g-67dcf231c018819189d16359637131e1-codul-media-audiovizuale-in-moldova)\n"
        "*Planul European de Dezvoltare 2030*\n"
        "[Deschide](https://chatgpt.com/g/g-67ddf0a103e0819188cc4ecc65065920-consultant-in-planul-european-de-dezvoltare)\n"
        "*Cod Penal Moldova*\n"
        "[Deschide](https://chatgpt.com/g/g-JzyqbkTOY-consultant-cod-penal-din-moldova)\n\n"

        "*🔹 Business, Istorie & Marketing*\n"
        "*Idei de Afaceri*\n"
        "[Deschide](https://chatgpt.com/g/g-6833013a49a88191a22c171078845641-idei-de-afaceri-online)\n"
        "*Moldova AI*\n"
        "[Deschide](https://chatgpt.com/g/g-6832f53407708191a77282090c293080-moldova-ai)\n"
        "*Marketing Trends Moldova*\n"
        "[Deschide](https://chatgpt.com/g/g-6802ea2fd07081919bb26ec62ec6637e-moldova-marketing-trends)\n\n"

        "*✍️ TEXTE & SCRIERE*\n"
        "*Scriitor Stilou*\n"
        "[Deschide](https://chatgpt.com/g/g-By7NIv7RT-scriitor-stilou)\n"
        "*Scriere Paradoxală*\n"
        "[Deschide](https://chatgpt.com/g/g-MwzAexdkx-writer-descrieri-paradoxale)\n"
        "*Personaj Negativ*\n"
        "[Deschide](https://chatgpt.com/g/g-kECr7SO90-writer-personaj-negativ)\n"
        "*Titluri ca Galben*\n"
        "[Deschide](https://chatgpt.com/g/g-tT0AFBLl4-scrie-titluri-ca-galben)\n\n"

        "*Meaning Architect*\n"
        "[Deschide](https://chatgpt.com/g/g-67556a497658819199b421c242ece94d-meaning-architect)\n"
        "*Narrio - Speak, Write, Publish*\n"
        "[Deschide](https://chatgpt.com/g/g-67556fc755848191a69aa350fbef4f78-narrio-speak-write-publish)\n"
        "*Story Gram - Engage, Inspire, Convert*\n"
        "[Deschide](https://chatgpt.com/g/g-675573f5e6d881919f82fd433f99e100-story-gram-engage-inspire-convert)"
    )

    await update.message.reply_text(text, parse_mode='Markdown')
