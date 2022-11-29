#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import telebot
from telegram_bot.bot import run_bot


load_dotenv()


def main():
    bot = telebot.TeleBot(str(os.getenv('BOT_TOKEN')), parse_mode='MARKDOWN')
    bot.set_my_commands([
        telebot.types.BotCommand("/help", "Как пользоваться ботом?"),
        telebot.types.BotCommand("/pick", "Выбрать языковую пару"),
        telebot.types.BotCommand("/current", "Активная языковая пара"),
    ])
    run_bot(bot=bot)
    bot.infinity_polling()


if __name__ == '__main__':
    main()
