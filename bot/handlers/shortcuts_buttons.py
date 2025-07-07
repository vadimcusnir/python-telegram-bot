from telegram.ext import MessageHandler, filters
from bot.handlers.review import review
from bot.handlers.notadoi import notadoi
from bot.handlers.contact import contact
from bot.handlers.public_gpts import public_gpts
from bot.handlers.diagnostic import start_diagnostic

def get_shortcut_handlers():
    return [
        MessageHandler(filters.TEXT & filters.Regex("(?i)diagnostic"), start_diagnostic),
        MessageHandler(filters.TEXT & filters.Regex("(?i)contact"), contact),
        MessageHandler(filters.TEXT & filters.Regex("(?i)gpts"), public_gpts),
        MessageHandler(filters.TEXT & filters.Regex("(?i)lounge"), review),
    ]
