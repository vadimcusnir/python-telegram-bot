from telegram.ext import MessageHandler, filters
from handlers.review import review
from handlers.notadoi import notadoi
from handlers.contact import contact
from handlers.public_gpts import public_gpts
from handlers.diagnostic import start_diagnostic

def get_shortcut_handlers():
    return [
        MessageHandler(filters.TEXT & filters.Regex("(?i)diagnostic"), start_diagnostic),
        MessageHandler(filters.TEXT & filters.Regex("(?i)contact"), contact),
        MessageHandler(filters.TEXT & filters.Regex("(?i)gpts"), public_gpts),
        MessageHandler(filters.TEXT & filters.Regex("(?i)lounge"), review),
    ]
