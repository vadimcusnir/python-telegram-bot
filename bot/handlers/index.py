# index.py – Înregistrează comenzile /start și /help

from telegram.ext import CommandHandler
from .start import start, help_message

from telegram.ext import CommandHandler
from .start import start
from .start import help_message

def get_index_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("help", help_message)
    ]

def index():
    return {
        "start": CommandHandler("start", start),
        "help": CommandHandler("help", help_message)
    }
