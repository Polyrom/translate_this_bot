#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import telebot
from telegram_bot.bot import run_bot


load_dotenv()


def main():
    bot = telebot.TeleBot(str(os.getenv('BOT_TOKEN')), parse_mode='MARKDOWN')
    run_bot(bot=bot)
    bot.infinity_polling()


if __name__ == '__main__':
    main()
