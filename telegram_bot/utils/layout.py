from telebot import types
from telegram_bot.utils import messages


def make_inline_langs_keyboard(lang_type):
    LANG_CODES = [
        'en', 'ru', 'de', 'fr',
        'it', 'es', 'pt', 'tr'
    ]
    keyboard = types.InlineKeyboardMarkup()
    for lang_code in LANG_CODES:
        keyboard.add(types.InlineKeyboardButton(
            messages.LANGUAGES[lang_code], callback_data=f'{lang_type}-{lang_code}'
        ))
    return keyboard
